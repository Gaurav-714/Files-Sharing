from rest_framework import serializers
from .models import *
import shutil


class FileSerializer(serializers.Serializer):
    class Meta:
        model = File
        fields = '__all__'


class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 100000, allow_empty_file = False, use_url = False)
    )
    folder = serializers.CharField(required = False)

    def zip_files(self, folder):
        shutil.make_archive(
            f'public/static/zip/{folder}', # name of the archive to be created.
            'zip',                         # specifies the type of archive to create, in this case, 'zip'.
            f'public/static/{folder}'      # path to the folder that needs to be zipped.
        )        

    def create(self, validated_data):
        try:
            folder = Folder.objects.create()
            #files = validated_data.pop('files')
            files = validated_data.get('files', [])  # Safely retrieve the 'files' list from validated_data
            file_objs = []
            for file_data in files:
                file_obj = File.objects.create(folder = folder, file = file_data)
                file_objs.append(file_obj)

            self.zip_files(folder.uid)
            return {'files' : {}, 'folder' : str(folder.uid)}
        
        except Exception as ex:
            raise serializers.ValidationError(f"Error occurred while creating files: {str(ex)}")