from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .models import Variant, Poll, Answer

class PollListView(ListView):
    model = Poll
    context_object_name = 'polls'
    template_name = 'polls/index.html'

class PollFormView(View):
    def get(self, request, id):
        poll = Poll.objects.get(id=id)

        return render(request, 'polls/form.html', context={
            "variants": poll.variants.all(),
            'poll': poll
        })

    def post(self, request, id):
        poll = Poll.objects.get(id=id)
        variant = request.POST.get('variant')
        variant_model = Variant.objects.get(id=variant)
        Answer.objects.create(
            variant=variant_model,
            poll=poll
        )
        return redirect('results', variant_model.poll.id)

class PollResultsView(View):
    def get(self, request, id):
        poll = Poll.objects.get(id=id)
        variants = poll.variants.all()
        all_answers= Answer.objects.filter(poll=poll)
        all_answers_count = len(all_answers)

        results = []

        for i in variants:
            variant_answers_count = len([j for j in all_answers if j.variant.id == i.id])
            percent = int((variant_answers_count / all_answers_count) * 100)
            res = {
                'text': i.name,
                'percentage': percent
            }
            results.append(res)

        return render(request, 'polls/results.html', context={
            'results': results
        })





