# Generated by Django 3.2.20 on 2024-03-12 09:22

import core.model_utils
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0041_auto_20231207_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalrepository',
            name='support_copy_paste',
        ),
        migrations.RemoveField(
            model_name='repository',
            name='support_copy_paste',
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=core.model_utils.JanewayBleachField(verbose_name='Write your comment:'),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='about',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='accept_version',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='decline',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='decline_version',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='file_upload_help',
            field=core.model_utils.JanewayBleachField(blank=True, help_text='Add any information that the author may need to know as part of the file upload process.', null=True, verbose_name='File Upload Help'),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='footer',
            field=core.model_utils.JanewayBleachField(blank=True, default='<p>Powered by Janeway</p>', null=True),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='login_text',
            field=core.model_utils.JanewayBleachField(blank=True, help_text='If text is added it will display on the login and register pages.', null=True, verbose_name='Account Page Text'),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='manager_review_status_change',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='new_comment',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='publication',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='require_pdf_help',
            field=core.model_utils.JanewayBleachField(blank=True, default='requires that all author uploads be PDF files.', help_text='When a repository requires that all manuscripts be PDF this text is combined with the repository name and displayed with the default text it would diplay: RepositoryName requires that all author uploads be PDF files.', null=True, verbose_name='Limit Upload to PDF Help'),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='review_helper',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='review_invitation',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='reviewer_review_status_change',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='start',
            field=core.model_utils.JanewayBleachField(blank=True, null=True, verbose_name='Submission Start Text'),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='submission',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='submission_access_request_text',
            field=core.model_utils.JanewayBleachField(blank=True, help_text='Describe any supporting information you want users to supply when requestingaccess permissions for this repository. Linked to Limit Access to Submissions.', null=True),
        ),
        migrations.AlterField(
            model_name='historicalrepository',
            name='submission_agreement',
            field=core.model_utils.JanewayBleachField(default='<p>Authors grant us the right to publish, on this website, their uploaded manuscript, supplementary materials and any supplied metadata.</p>', help_text="Add any information that the author may need to know as part of their submission, eg. Copyright transfer etc.'", null=True),
        ),
        migrations.AlterField(
            model_name='preprint',
            name='abstract',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='preprint',
            name='preprint_decline_note',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='preprintversion',
            name='abstract',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='about',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='accept_version',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='decline',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='decline_version',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='file_upload_help',
            field=core.model_utils.JanewayBleachField(blank=True, help_text='Add any information that the author may need to know as part of the file upload process.', null=True, verbose_name='File Upload Help'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='footer',
            field=core.model_utils.JanewayBleachField(blank=True, default='<p>Powered by Janeway</p>', null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='login_text',
            field=core.model_utils.JanewayBleachField(blank=True, help_text='If text is added it will display on the login and register pages.', null=True, verbose_name='Account Page Text'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='manager_review_status_change',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='new_comment',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='publication',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='require_pdf_help',
            field=core.model_utils.JanewayBleachField(blank=True, default='requires that all author uploads be PDF files.', help_text='When a repository requires that all manuscripts be PDF this text is combined with the repository name and displayed with the default text it would diplay: RepositoryName requires that all author uploads be PDF files.', null=True, verbose_name='Limit Upload to PDF Help'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='review_helper',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='review_invitation',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='reviewer_review_status_change',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='start',
            field=core.model_utils.JanewayBleachField(blank=True, null=True, verbose_name='Submission Start Text'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='submission',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='submission_access_request_text',
            field=core.model_utils.JanewayBleachField(blank=True, help_text='Describe any supporting information you want users to supply when requestingaccess permissions for this repository. Linked to Limit Access to Submissions.', null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='submission_agreement',
            field=core.model_utils.JanewayBleachField(default='<p>Authors grant us the right to publish, on this website, their uploaded manuscript, supplementary materials and any supplied metadata.</p>', help_text="Add any information that the author may need to know as part of their submission, eg. Copyright transfer etc.'", null=True),
        ),
        migrations.AlterField(
            model_name='repositoryfield',
            name='help_text',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='status_reason',
            field=core.model_utils.JanewayBleachField(blank=True, help_text='Information supplied by a reviewer when declining or completing a review or by staff withdrawing a review', null=True),
        ),
        migrations.AlterField(
            model_name='versionqueue',
            name='abstract',
            field=core.model_utils.JanewayBleachField(blank=True, null=True),
        ),
    ]
