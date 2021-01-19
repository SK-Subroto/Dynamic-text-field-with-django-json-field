def job(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'portal/job.html', context)




@api_view(['POST'])
def jobCreate(request):
    attendant_user = Attendant.objects.get(user__id=request.user.id)
    print(attendant_user)
    job_data = request.data
    print(job_data)
    new_job = Job.objects.create(attendant=attendant_user,
                                 title=job_data["title"],
                                 company_name=job_data["c_name"],
                                 company_logo=job_data["c_logo"],
                                 deadline=job_data["deadline"],
                                 requirements=job_data["requirement"]
                                 )
    new_job.save()
    serializer = JobSerializer(new_job)
    # serializer = NoticeSerializer(data=request.data)

    # if serializer.is_valid():
    #     serializer.save()

    return Response(serializer.data)