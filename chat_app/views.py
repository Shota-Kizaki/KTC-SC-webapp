import os
from dotenv import load_dotenv
from django.shortcuts import render
import openpyxl
from django.http import HttpResponse
from django.utils.timezone import make_naive, get_default_timezone
from django.utils.dateparse import parse_date
from .templatetags.custom_filters import group_required
from chat_app.models import ChatLog
from django.contrib.auth.models import User
from django.utils.dateparse import parse_date
from .application.memory import get_contexts
from langchain.memory import ConversationBufferMemory
from django.contrib.auth.decorators import login_required
from .application import agents

load_dotenv(override=True)

#チャット画面を表示する
@login_required
def chat(request):
    if request.method == 'POST' and request.POST.get('question'):
        input_text = request.POST.get('question')
        user_id = request.user.id  # ログイン中のユーザーのIDを取得
        if input_text:  # 質問がある場合のみ処理
            # run関数を呼び出す
            memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
            contexts = get_contexts(user_id)
            for context in contexts:
                memory.save_context({"input": context["question"]}, {"output": context["answer"]})
            agent = agents.MainAgent(memory=memory, verbose=True)
            result = agent.run(input_text)
            ChatLog.objects.create(user=request.user, question=input_text, answer=result)

    chat_logs = ChatLog.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'chat_app/chat.html', {'chat_logs': chat_logs})

#ログを表示する
def log_list(request):
    logs = ChatLog.objects.all()

    # ユーザーによるフィルタリング
    user_id = request.user.id
    if user_id:
        logs = logs.filter(user_id=user_id)

    # 日付によるフィルタリング
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date:
        start_date = parse_date(start_date)
        logs = logs.filter(created_at__date__gte=start_date)
    if end_date:
        end_date = parse_date(end_date)
        logs = logs.filter(created_at__date__lte=end_date)

    context = {
        'logs': logs,
        'users': User.objects.all(),
    }
    return render(request, 'chat_app/log_list.html', context)


#ダウンロード機能


@group_required('管理者')
def download_logs(request):
    # フィルタリング条件の取得
    user_id = request.GET.get('user')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # ログデータのフィルタリング
    logs = ChatLog.objects.all().select_related('user')
    if user_id:
        logs = logs.filter(user_id=user_id)
    if start_date:
        start_date = parse_date(start_date)
        logs = logs.filter(created_at__date__gte=start_date)
    if end_date:
        end_date = parse_date(end_date)
        logs = logs.filter(created_at__date__lte=end_date)

    # 新しいワークブックの作成
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Logs"

    # ヘッダー行の追加
    columns = ["日付", "ユーザー名", "質問", "回答"]
    ws.append(columns)

    # ログデータの追加
    for log in logs:
        naive_datetime = make_naive(log.created_at, timezone=get_default_timezone())
        ws.append([naive_datetime, log.user.username, log.question, log.answer])

    # レスポンスとしてExcelファイルを返す
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=logs.xlsx'
    wb.save(response)

    return response

    