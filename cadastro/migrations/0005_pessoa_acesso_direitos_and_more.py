# Generated by Django 5.0.4 on 2024-04-13 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_alter_pessoa_options_remove_pessoa_cidade_origem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='acesso_direitos',
            field=models.BooleanField(default=False, verbose_name='Acesso a Direitos'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='acesso_direitos_assistencia_social',
            field=models.BooleanField(default=False, verbose_name='Acesso a Direitos (Assistência Social)'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='acesso_direitos_documentacao_familiares',
            field=models.BooleanField(default=False, verbose_name='Acesso a Direitos (Documentação para familiares)'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='acesso_direitos_educacao',
            field=models.BooleanField(default=False, verbose_name='Acesso a Direitos (Educação)'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='acesso_direitos_outros_apoios_documentacao',
            field=models.BooleanField(default=False, verbose_name='Acesso a Direitos (Outros apoios com documentação)'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='acesso_direitos_saude',
            field=models.BooleanField(default=False, verbose_name='Acesso a Direitos (Saúde)'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='acesso_direitos_trabalho',
            field=models.BooleanField(default=False, verbose_name='Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='apoio_trabalho_preparo_curriculo_vagas',
            field=models.BooleanField(default=False, verbose_name='Apoio com trabalho (preparo de currículo e vagas de trabalho)'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='atividade_servico_1',
            field=models.CharField(blank=True, choices=[('', 'Selecione...'), ('Acesso a Direitos', 'Acesso a Direitos'), ('Acesso a Direitos (Assistência Social)', 'Acesso a Direitos (Assistência Social)'), ('Acesso a Direitos (Documentação para familiares)', 'Acesso a Direitos (Documentação para familiares)'), ('Acesso a Direitos (Educação)', 'Acesso a Direitos (Educação)'), ('Acesso a Direitos (Outros apoios com documentação)', 'Acesso a Direitos (Outros apoios com documentação)'), ('Acesso a Direitos (Saúde)', 'Acesso a Direitos (Saúde)'), ('Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)', 'Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)'), ('Apoio com trabalho (preparo de currículo e vagas de trabalho)', 'Apoio com trabalho (preparo de currículo e vagas de trabalho)'), ('Aulas de Português', 'Aulas de Português'), ('Cursos de informática e tecnologia', 'Cursos de informática e tecnologia'), ('Regularização migratória (apoio com renovação ou solicitação de documentos)', 'Regularização migratória (apoio com renovação ou solicitação de documentos)')], max_length=100, null=True, verbose_name='Atividade/Serviço Solicitado 1'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='atividade_servico_2',
            field=models.CharField(blank=True, choices=[('', 'Selecione...'), ('Acesso a Direitos', 'Acesso a Direitos'), ('Acesso a Direitos (Assistência Social)', 'Acesso a Direitos (Assistência Social)'), ('Acesso a Direitos (Documentação para familiares)', 'Acesso a Direitos (Documentação para familiares)'), ('Acesso a Direitos (Educação)', 'Acesso a Direitos (Educação)'), ('Acesso a Direitos (Outros apoios com documentação)', 'Acesso a Direitos (Outros apoios com documentação)'), ('Acesso a Direitos (Saúde)', 'Acesso a Direitos (Saúde)'), ('Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)', 'Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)'), ('Apoio com trabalho (preparo de currículo e vagas de trabalho)', 'Apoio com trabalho (preparo de currículo e vagas de trabalho)'), ('Aulas de Português', 'Aulas de Português'), ('Cursos de informática e tecnologia', 'Cursos de informática e tecnologia'), ('Regularização migratória (apoio com renovação ou solicitação de documentos)', 'Regularização migratória (apoio com renovação ou solicitação de documentos)')], max_length=100, null=True, verbose_name='Atividade/Serviço Solicitado 2'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='atividade_servico_3',
            field=models.CharField(blank=True, choices=[('', 'Selecione...'), ('Acesso a Direitos', 'Acesso a Direitos'), ('Acesso a Direitos (Assistência Social)', 'Acesso a Direitos (Assistência Social)'), ('Acesso a Direitos (Documentação para familiares)', 'Acesso a Direitos (Documentação para familiares)'), ('Acesso a Direitos (Educação)', 'Acesso a Direitos (Educação)'), ('Acesso a Direitos (Outros apoios com documentação)', 'Acesso a Direitos (Outros apoios com documentação)'), ('Acesso a Direitos (Saúde)', 'Acesso a Direitos (Saúde)'), ('Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)', 'Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)'), ('Apoio com trabalho (preparo de currículo e vagas de trabalho)', 'Apoio com trabalho (preparo de currículo e vagas de trabalho)'), ('Aulas de Português', 'Aulas de Português'), ('Cursos de informática e tecnologia', 'Cursos de informática e tecnologia'), ('Regularização migratória (apoio com renovação ou solicitação de documentos)', 'Regularização migratória (apoio com renovação ou solicitação de documentos)')], max_length=100, null=True, verbose_name='Atividade/Serviço Solicitado 3'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='atividade_servico_4',
            field=models.CharField(blank=True, choices=[('', 'Selecione...'), ('Acesso a Direitos', 'Acesso a Direitos'), ('Acesso a Direitos (Assistência Social)', 'Acesso a Direitos (Assistência Social)'), ('Acesso a Direitos (Documentação para familiares)', 'Acesso a Direitos (Documentação para familiares)'), ('Acesso a Direitos (Educação)', 'Acesso a Direitos (Educação)'), ('Acesso a Direitos (Outros apoios com documentação)', 'Acesso a Direitos (Outros apoios com documentação)'), ('Acesso a Direitos (Saúde)', 'Acesso a Direitos (Saúde)'), ('Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)', 'Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)'), ('Apoio com trabalho (preparo de currículo e vagas de trabalho)', 'Apoio com trabalho (preparo de currículo e vagas de trabalho)'), ('Aulas de Português', 'Aulas de Português'), ('Cursos de informática e tecnologia', 'Cursos de informática e tecnologia'), ('Regularização migratória (apoio com renovação ou solicitação de documentos)', 'Regularização migratória (apoio com renovação ou solicitação de documentos)')], max_length=100, null=True, verbose_name='Atividade/Serviço Solicitado 4'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='atividade_servico_5',
            field=models.CharField(blank=True, choices=[('', 'Selecione...'), ('Acesso a Direitos', 'Acesso a Direitos'), ('Acesso a Direitos (Assistência Social)', 'Acesso a Direitos (Assistência Social)'), ('Acesso a Direitos (Documentação para familiares)', 'Acesso a Direitos (Documentação para familiares)'), ('Acesso a Direitos (Educação)', 'Acesso a Direitos (Educação)'), ('Acesso a Direitos (Outros apoios com documentação)', 'Acesso a Direitos (Outros apoios com documentação)'), ('Acesso a Direitos (Saúde)', 'Acesso a Direitos (Saúde)'), ('Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)', 'Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)'), ('Apoio com trabalho (preparo de currículo e vagas de trabalho)', 'Apoio com trabalho (preparo de currículo e vagas de trabalho)'), ('Aulas de Português', 'Aulas de Português'), ('Cursos de informática e tecnologia', 'Cursos de informática e tecnologia'), ('Regularização migratória (apoio com renovação ou solicitação de documentos)', 'Regularização migratória (apoio com renovação ou solicitação de documentos)')], max_length=100, null=True, verbose_name='Atividade/Serviço Solicitado 5'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='aulas_portugues',
            field=models.BooleanField(default=False, verbose_name='Aulas de Português'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='bairro',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cidade',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cursos_informatica_tecnologia',
            field=models.BooleanField(default=False, verbose_name='Cursos de informática e tecnologia'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Endereço Residencial (Nome da rua e número da casa)'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='estado',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='regularizacao_migratoria',
            field=models.BooleanField(default=False, verbose_name='Regularização migratória (apoio com renovação ou solicitação de documentos)'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='situacao_migratoria',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Situação Migratória'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='telefone_trabalho',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone do Trabalho'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='idade',
            field=models.IntegerField(blank=True, null=True, verbose_name='Idade'),
        ),
    ]
