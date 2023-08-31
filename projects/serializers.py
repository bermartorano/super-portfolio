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


class CertificateNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['name']


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = CertificateNestedSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = "__all__"

    def create(self, validated_data):
        C_INST = "certifying_institution"
        certificates_data = validated_data.pop("certificates")
        certifying_inst = CertifyingInstitution.objects.create(
            **validated_data)
        for certificate in certificates_data:
            certificate[C_INST] = certifying_inst
            CertificateSerializer().create(
                validated_data=certificate)

        return certifying_inst
