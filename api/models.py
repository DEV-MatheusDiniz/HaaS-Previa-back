from django.db import models
from simple_history.models import HistoricalRecords

from django.contrib.auth.base_user import AbstractBaseUser
import uuid

from django.contrib.auth.base_user import BaseUserManager


def jwt_get_secret_key(user_model):
    return user_model.jwt_secret


class UsuarioManager(BaseUserManager):
    def create_user(self, ds_email, password, no_usuario, grupo, is_active):

        if not ds_email:
            raise ValueError('Os usuários devem ter um endereço e-mail')

        user = self.model(ds_email=self.normalize_email(
            ds_email), no_usuario=no_usuario, grupo=grupo, is_active=is_active)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, ds_email, password, no_usuario, grupo, is_active):
        """
        Creates and saves a superuser with the given ds_email and
        password.
        """
        user = self.create_user(
            ds_email, password, no_usuario, grupo, is_active)
        user.is_admin = True
        user.save(using=self._db)
        return user


class UsuarioGrupo(models.Model):
    id = models.IntegerField(primary_key=True)
    no_grupo = models.CharField(max_length=100, null=False)
    ds_tag = models.CharField(max_length=50, null=False)
    bo_tem_regra = models.BooleanField(default=True, null=False)
    st_ambiente = models.CharField(max_length=7, null=False)
    bo_ativo = models.BooleanField(default=True, null=False)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords(
        table_name='historico\".\"usuario_grupo_history')

    class Meta:
        app_label = 'api'
        db_table = 'cliente\".\"usuario_grupo'
        indexes = [
            models.Index(fields=['id'], name='c_usrgrp_id_idx'),
            models.Index(fields=['no_grupo'], name='c_usrgrp_no_grupo_idx'),
            models.Index(fields=['ds_tag'], name='c_usrgrp_ds_tag_idx'),
            models.Index(fields=['bo_tem_regra'],
                         name='c_usrgrp_bo_tem_regra_idx'),
            models.Index(fields=['st_ambiente'],
                         name='c_usrgrp_st_ambiente_idx'),
            models.Index(fields=['bo_ativo'], name='c_usrgrp_bo_ativo_idx'),
            models.Index(fields=['dt_alteracao'],
                         name='c_usrgrp_dt_alteracao_idx'),
            models.Index(fields=['dt_cadastro'],
                         name='c_usrgrp_dt_cadastro_idx'),
        ]


class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(
        UsuarioGrupo, related_name='UsuarioGrupoUsuario', on_delete=models.PROTECT)
    no_usuario = models.CharField(max_length=150, null=False)
    ds_email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    jwt_secret = models.UUIDField(default=uuid.uuid4)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords(
        table_name='historico\".\"usuario_history')

    objects = UsuarioManager()

    REQUIRED_FIELDS = ['no_usuario', 'grupo', 'is_active']

    USERNAME_FIELD = 'ds_email'

    class Meta:
        app_label = 'api'
        db_table = 'cliente\".\"usuario'
        indexes = [
            models.Index(fields=['id'], name='c_usr_id_idx'),
            models.Index(fields=['no_usuario'], name='c_usr_no_usuario_idx'),
            models.Index(fields=['ds_email'], name='c_usr_ds_email_idx'),
            models.Index(fields=['password'], name='c_usr_password_idx'),
            models.Index(fields=['last_login'], name='c_usr_is_admin_idx'),
            models.Index(fields=['is_admin'], name='c_usr_is_active_idx'),
            models.Index(fields=['is_active'], name='c_usr_jwt_secret_idx'),
            models.Index(fields=['jwt_secret'], name='c_usr_last_login_idx'),
            models.Index(fields=['dt_alteracao'],
                         name='c_usr_dt_alteracao_idx'),
            models.Index(fields=['dt_cadastro'], name='c_usr_dt_cadastro_idx'),
        ]



class Contrato(models.Model):
    """
        o campo "tp_regra_cobranca", pode receber valor 'ic_porcentagem' ou 'ic_dia_faturar'

        ic_porcentagem => regra por %
        ic_dia_faturar => regra por dias (default)

        o campo "tp_relevancia", pode receber valor 'individual' ou 'grupo'

        individual => relevancia individual por IC`s
        grupo => relevancia por grupo do IC`s  (default)

    """
    id = models.IntegerField(primary_key=True)
    no_entidade = models.CharField(max_length=150, null=False)
    no_contrato = models.CharField(max_length=150, null=False)
    vl_unidade_servico = models.DecimalField(
        max_digits=12, decimal_places=2, null=False)
    nu_dia_faturamento = models.CharField(max_length=2, null=False)
    tp_regra_cobranca = models.CharField(
        max_length=14, default='ic_dia_faturar', null=False)
    tp_relevancia = models.CharField(
        max_length=10, default='grupo', null=False)
    bo_ativo = models.BooleanField(default=True, null=False)
    dt_sincronizacao = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords(
        table_name='historico\".\"contrato_history')

    class Meta:
        app_label = 'api'
        db_table = 'cliente\".\"contrato'
        indexes = [
            models.Index(fields=['id'], name='c_ctr_id_idx'),
            models.Index(fields=['no_entidade'], name='c_ctr_no_entidade_idx'),
            models.Index(fields=['no_contrato'], name='c_ctr_no_contrato_idx'),
            models.Index(fields=['tp_regra_cobranca'],
                         name='c_ctr_tp_rg_cbr_idx'),
            models.Index(fields=['tp_relevancia'], name='c_ctr_tp_rlvc_idx'),
            models.Index(fields=['vl_unidade_servico'],
                         name='c_ctr_vl_unidade_servico_idx'),
            models.Index(fields=['nu_dia_faturamento'],
                         name='c_ctr_nu_dia_faturamento_idx'),
            models.Index(fields=['bo_ativo'], name='c_ctr_bo_ativo_idx'),
            models.Index(fields=['dt_sincronizacao'],
                         name='c_ctr_dt_szc_idx'),
        ]


class Faturamento(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(
        Usuario, related_name='FaturamentoUsuario', on_delete=models.PROTECT, null=True, blank=True)
    contrato = models.ForeignKey(
        Contrato, related_name='FaturamentoContrato', on_delete=models.PROTECT)
    vl_unidade_servico = models.DecimalField(
        max_digits=12, decimal_places=2, null=True)
    bo_regra_cobranca = models.BooleanField(default=False, null=False)
    qt_contabilizado = models.IntegerField(null=False)
    qt_nao_contabilizado = models.IntegerField(null=True, blank=True)
    qt_relevancia_sem_validacao = models.IntegerField(default=0, null=True)
    vl_total_unitario = models.DecimalField(
        max_digits=12, decimal_places=2, null=False)
    vl_total_grupo = models.DecimalField(
        max_digits=12, decimal_places=2, null=False)
    vl_total_mensal = models.DecimalField(
        max_digits=12, decimal_places=2, null=False)
    dt_mes_referencia = models.DateField(null=False)
    ds_observacao = models.CharField(max_length=255, null=True, blank=True)
    st_situacao = models.CharField(max_length=9, default='previa', null=False)
    bo_diario = models.BooleanField(default=False, null=False)
    bo_faturado = models.BooleanField(default=False, null=False)
    dt_faturado = models.DateTimeField(auto_now=True, null=True, blank=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)
    dt_inicial_simulacao = models.DateTimeField(null=True, blank=True)
    dt_final_simulacao = models.DateTimeField(null=True, blank=True)
    dt_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'api'
        db_table = 'cliente\".\"faturamento'
        indexes = [
            models.Index(fields=['id'], name='c_ftr_id_idx'),
            models.Index(fields=['bo_regra_cobranca'],
                         name='c_ftr_bo_regra_cobranca_idx'),
            models.Index(fields=['vl_unidade_servico'],
                         name='c_ftr_vl_unidade_servico_idx'),
            models.Index(fields=['qt_contabilizado'],
                         name='c_ftr_qt_contabilizado_idx'),
            models.Index(fields=['qt_nao_contabilizado'],
                         name='c_ftr_qt_nao_contabilizado_idx'),
            models.Index(fields=['qt_relevancia_sem_validacao'],
                         name='c_ftr_qt_rlv_s_vali_idx'),
            models.Index(fields=['vl_total_unitario'],
                         name='c_ftr_vl_total_unitario_idx'),
            models.Index(fields=['vl_total_grupo'],
                         name='c_ftr_vl_total_grupo_idx'),
            models.Index(fields=['vl_total_mensal'],
                         name='c_ftr_vl_total_mensal_idx'),
            models.Index(fields=['dt_mes_referencia'],
                         name='c_ftr_dt_mes_referencia_idx'),
            models.Index(fields=['bo_faturado'], name='c_ftr_bo_faturado_idx'),
            models.Index(fields=['st_situacao'], name='c_ftr_st_situacao_idx'),
            models.Index(fields=['bo_diario'], name='c_ftr_bo_diario_idx'),
            models.Index(fields=['dt_faturado'], name='c_ftr_dt_faturado_idx'),
            models.Index(fields=['dt_alteracao'],
                         name='c_ftr_dt_alteracao_idx'),
            models.Index(fields=['dt_cadastro'], name='c_ftr_dt_cadastro_idx'),
        ]
