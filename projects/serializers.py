from rest_framework import serializers
from .models import Profile, Project, Certificate, CertifyingInstitution


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = "__all__"

    def create(self, validated_data):
        print("********** começo do create")
        C_INST = "certifying_institution"
        certificates_data = validated_data.pop("certificates")
        certtifying_inst = CertifyingInstitution.objects.create(
            **validated_data)
        print("********** criação do CI")
        for certificate in certificates_data:
            certificate_and_institution = {
                **certificate,
                C_INST: certtifying_inst}
            CertificateSerializer().create(
                validated_data=certificate_and_institution)

        return certtifying_inst
