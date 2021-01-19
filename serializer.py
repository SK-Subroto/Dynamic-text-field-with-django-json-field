class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'
