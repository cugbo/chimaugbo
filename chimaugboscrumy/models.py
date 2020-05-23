def move_goal(request, goal_id):
    message = {'error': 'A record with that goal id does not exist'}
    try:
        obj = ScrumyGoals.objects.get(id=goal_id)
    except Exception as e:
        return render(request, 'chimaugboscrumy/exception.html', message)
    else:
        return HttpResponse(obj.goal_name)


def add_goal(request):
    already_used = []
    number = randint(1000, 9999)
    if number not in already_used:
        addgoal = ScrumyGoals.objects.create(goal_name='Keep Learning Django',
                                             goal_id=number,
                                             created_by='Louis',
                                             moved_by='Louis', owner='Louis',
                                             goal_status=GoalStatus.objects.get
                                             (status_name='Weekly Goal'),
                                             user=User.objects.get(
                                                 username='Louis Oma')
                                             )
        already_used.append(number)
    return HttpResponse(addgoal)

def home (request):
    objs = ScrumyGoals.objects.all()
    myuser = User.objects.all()
    dictionary = {
        'goal_name': objs.goal_name_set,
        'goal_id': '1',
        'user': User.objects.goal_name(first_name='Louis'),
    }
    return render(request, 'chimaugboscrumy/home.html', dictionary)
