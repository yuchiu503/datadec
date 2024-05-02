from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question
from django.template import loader
from django.http import Http404
from .models import Choice, Question
from django.db.models import F
from django.urls import reverse
from django.views import generic

# Create your views here.

# 常规视图设置————————————————————————————————————————————————————————————————————————————

def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    #「载入模板，填充上下文，再返回由它生成的 HttpResponse 对象」
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # 使用render快捷函数
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)



def detail(request,question_id):
    # return HttpResponse(f"你在查看{question_id}问题")
    #正常返回404错误
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("问题不存在")
    # return render(request, "polls/detail.html", {"question": question})

    #使用get_object_or_404返回404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})



def results(request,question_id):
    # return HttpResponse(f"你在查看{question_id}问题的结果")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "你没有选择",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    

#以上是常规视图设置——————————————————————————————————————————————————————————————————


# 采用通用视图系统编写views函数

# class IndexView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """返回最近发布的五个问题"""
#         return Question.objects.order_by("-pub_date")[:5]
    
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "polls/detail.html"

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = "polls/results.html"

# def vote(request, question_id):