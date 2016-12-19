# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 15:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinValDefs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('coin_value', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Coin Value')),
                ('coin_volume', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Coin Volume')),
                ('coin_val_parms', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('01', 'Enable Coin Window'), ('02', 'Accept Coin')], max_length=5, null=True, verbose_name='Coin Parameters')),
            ],
            options={
                'verbose_name_plural': 'Coin Validator Coin Definitions',
                'verbose_name': 'Coin Validator Coin Definition',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='CoinValTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('cash_box_volume', models.PositiveIntegerField(default=20800, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Cashbox Volume')),
                ('escrow_volume', models.PositiveIntegerField(default=600, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Escrow Volume')),
                ('cash_box_volume_threshold', models.PositiveIntegerField(default=16640, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Cashbox Volume Threshold')),
                ('cash_box_value_threshold', models.BigIntegerField(default=25000, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4294967295), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Cashbox Value Threshold')),
                ('escrow_volume_threshold', models.PositiveIntegerField(default=600, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Escrow Volume Threshold')),
                ('escrow_value_threshold', models.BigIntegerField(default=600, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4294967295), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Escrow Value Threshold')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'verbose_name_plural': 'Coin Validator Paramters',
                'verbose_name': 'Coin Validator Paramters',
            },
        ),
        migrations.CreateModel(
            name='FconfigOpts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('terminal_type', models.PositiveSmallIntegerField(choices=[('00', 'Unknwon Terminal Type'), ('01', 'Card Type Terminal'), ('02', 'Universal Type Terminal'), ('03', 'Coin Terminal Type'), ('03', 'Maximim Terminal Type'), ('10', 'Smart Card Terminal Type')], default='02', verbose_name='Terminal Type')),
                ('display_present', models.BooleanField(default=True, verbose_name='Display present')),
                ('num_call_follow_on', models.PositiveSmallIntegerField(blank=True, default=5, null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Number of Call follows')),
                ('card_validation_info', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('01', 'Auth for Local'), ('02', 'Delay Auth'), ('04', 'MCE Auth for Local'), ('08', 'International'), ('08', 'Insert NPA for 0+ Local/Intra'), ('10', 'Manually Entered Call Card'), ('00', 'ACCS Mode use NCC'), ('80', 'Validate after Number obtained')], default=['01', '04'], max_length=23, null=True, verbose_name='Card validation info')),
                ('accs_info', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('01', 'ACCS Mode is available'), ('02', 'Route MCE Calls via 0+ network'), ('04', 'MCE Feature enable'), ('08', 'MCE Calls MUST be NCC-validated'), ('10', 'AOS Feature enable'), ('20', 'Strip off leading 0/1'), ('80', 'Strip off local NPA')], default='01', max_length=20, null=True, verbose_name='ACCS-Mode/Info')),
                ('incoming_call_mode', models.PositiveSmallIntegerField(choices=[('0', 'Ringing disabled'), ('1', 'Ringing / Incoming Voice'), ('2', 'No Ringing / Data Call'), ('3', 'Ringing / Voice / Delayed Data Call')], default='1', verbose_name='Incoming Call mode')),
                ('incoming_call_anti_fraud', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('0', 'Answer Supervision')], default='0', max_length=1, null=True, verbose_name='Anti-Fraud for Incoming Call')),
                ('oos_pots_flags', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('01', 'Do not put Terminal Out-Of-Service when CDR list is full'), ('02', 'Display Rate (MTR 1.x: Only Card-Terminals)'), ('04', 'INCOMMING_CALL_FCA_PRECED'), ('08', 'FCA_ZERO_VALUE_CARD'), ('10', 'MTR 1.x: Spare 4 / MTR 2.x: Automatically revert to primary Modem pool'), ('20', 'MTR 1.x: Spare 5 / MTR 2.x: Block Carrier calls without nternal rate'), ('40', 'MTR 1.x: Spare 6 / MTR 2.x: Creditcard CDRs should contain the charged amount for the calls'), ('80', 'MTR 1.x: Spare 7 / MTR 2.x: Force 11-digit-dialing on local calls')], default=['01', '02', '04', '08'], max_length=23, null=True, verbose_name='Out-Of-Service POTS Flags')),
                ('data_jack_visual_display', models.BooleanField(default=False, verbose_name='Datajack visual display')),
                ('incoming_call_rate', models.PositiveSmallIntegerField(default=8, help_text='MTR1.x only', validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Incoming call rate')),
                ('language_scrolling_order', models.PositiveSmallIntegerField(choices=[('1', 'English'), ('2', 'French'), ('3', 'Spanish'), ('4', 'Japanese')], default='1', help_text='MTR 2.x only', verbose_name='Language Scrolling Order - 1st language')),
                ('spareB', models.PositiveSmallIntegerField(blank=True, help_text='MTR1.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Spare B')),
                ('language_scrolling_order_2', models.PositiveSmallIntegerField(choices=[('1', 'English'), ('2', 'French'), ('3', 'Spanish'), ('4', 'Japanese')], default='2', help_text='MTR 2.x only', verbose_name='Language Scrolling Order - 2nd language')),
                ('spareC', models.PositiveSmallIntegerField(blank=True, help_text='MTR1.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Spare C')),
                ('number_of_languages', models.PositiveSmallIntegerField(choices=[('1', '1 Language'), ('2', '2 Languages'), ('3', '3 Languages (MTR 2.x only)'), ('4', '4 Languages (MTR 2.x only)')], default='2', help_text='MTR2.x only', verbose_name='Number of Languages')),
                ('spareD', models.PositiveSmallIntegerField(blank=True, help_text='MTR1.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Spare D')),
                ('rating_flags', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('01', 'Enable NPA SBR'), ('02', 'Enable International SBR'), ('04', 'Enable Dial Around'), ('08', 'Show 1st xx min $, additional yy min $'), ('10', 'Round up charge'), ('20', '7-digit no-wait Option')], default=[], help_text='MTR2.x only', max_length=17, null=True, verbose_name='Rating Flags')),
                ('spareE', models.PositiveSmallIntegerField(blank=True, help_text='MTR1.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Spare E')),
                ('dial_around_timer', models.PositiveSmallIntegerField(blank=True, help_text='MTR2.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Dial-around timer')),
                ('spareF', models.PositiveSmallIntegerField(blank=True, help_text='MTR1.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Spare F')),
                ('opr_interntl_access_ptr', models.PositiveSmallIntegerField(blank=True, help_text='MTR2.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Pointer to international Access Operator')),
                ('aos_number', models.CharField(blank=True, help_text='MTR 1.x only', max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='AOS number')),
                ('aos_interlata_access', models.PositiveSmallIntegerField(blank=True, help_text='MTR2.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Pointer to Inter-LATA AOS-number')),
                ('aos_interntl_access', models.PositiveSmallIntegerField(blank=True, help_text='MTR2.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Pointer to International Access AOS-number')),
                ('djack_grace_before_collect', models.PositiveSmallIntegerField(blank=True, help_text='MTR2.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Datajack grace-periode before collection')),
                ('opr_collection_tmr', models.PositiveSmallIntegerField(blank=True, help_text='MTR2.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Operator collection timer\t')),
                ('opr_intralata_access_ptr', models.PositiveSmallIntegerField(blank=True, help_text='MTR2.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Pointer to Intra-LATA operator access number')),
                ('opr_interlata_access_ptr', models.PositiveSmallIntegerField(blank=True, help_text='MTR2.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Pointer to Inter-LATA operator access number')),
                ('advert_enable', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('01', 'On Hook Adverts enabled'), ('02', 'Repdialer Adverts enabled'), ('04', 'Call Established adverts enabled'), ('08', 'On Hook Date and Time displayed'), ('10', 'On Hook Date and Time displayed in 12hr Format')], default=['01'], max_length=14, null=True, verbose_name='Enable Advertising')),
                ('default_language', models.PositiveSmallIntegerField(choices=[('1', 'English'), ('2', 'French'), ('3', 'Spanish'), ('4', 'Japanese')], default='1', verbose_name='Default Language')),
                ('display_called_number', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('01', 'Display Called Number Prompt'), ('80', 'Surpress Calling Prompt')], default=['01'], max_length=5, null=True, verbose_name='Called Number Displaying')),
                ('dtmf_duration', models.PositiveSmallIntegerField(default=8, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='DTMF Duration')),
                ('inter_digit_pause', models.PositiveSmallIntegerField(default=8, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Inter-digit Pause')),
                ('dialing_conversion', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('01', 'Convert Operator to Toll'), ('02', 'Convert Toll to Operator')], default=['01', '02'], help_text='MTR 1.x only', max_length=5, null=True, verbose_name='Incoming Call mode')),
                ('ppu_pre_auth_credit_limit', models.PositiveSmallIntegerField(default=0, help_text='MTR 2.x only', validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='PPU PreAuth Credit Limit')),
                ('coin_call_features', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('01', 'Overtime'), ('02', 'Voice-Feedback'), ('04', '2nd Warning')], default=['02', '04'], max_length=8, null=True, verbose_name='Coin calling Features')),
                ('coin_call_overtime_period', models.PositiveIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Coin call overtime period')),
                ('coin_call_pots_time', models.PositiveIntegerField(default=120, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Coin call POTS time')),
                ('min_international_digits', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Minimum number of digits for international calls')),
                ('def_rate_req_payment', models.PositiveSmallIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='default rate request payment type')),
                ('next_call_revalidation_freq', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Next Call re-validation frequency')),
                ('cutoff_on_disconnect_duration', models.PositiveSmallIntegerField(default=45, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Cutoff on disconnect duration')),
                ('cdr_upload_timer_int', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='CDR Upload timer for international calls')),
                ('cdr_upload_timer_nonint', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='CDR Upload timer for non-international calls')),
                ('perf_stats_dialog_fails', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Number of performance statistics dialog fails')),
                ('co_line_check_fails', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Number of CO-line-check fails')),
                ('alt_ncc_dialog_fails', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Number of alternative NCC-dialog-check fails')),
                ('dialog_fails_till_oos', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Number of failed dialogues until Terminal goes Out-Of-Service')),
                ('dialog_fails_till_alarm', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Number of failed dialogues until alarm is sent')),
                ('smart_card_flags', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('20', 'POST_PAYMENT_RATE_REQUEST'), ('80', 'DLOG_FCG_SUPPRESS_TERMINAL_RATE_INFO')], default=['01'], max_length=5, null=True, verbose_name='Smartcard Flags')),
                ('max_man_card_dig', models.PositiveSmallIntegerField(default=14, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Maximum number of digits of manual card entry')),
                ('aos_intra_access_ptr', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Pointer to Intra-AOS access-number')),
                ('carrier_reroute_flags', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Carrier reroute-flags')),
                ('min_man_card_dig', models.PositiveSmallIntegerField(default=14, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Minimum number of digits of manual card entry')),
                ('max_smart_card_inserts', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Maximum number of smartcard-inserts')),
                ('max_diff_smart_card_inserts', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Maximum number of different smartcard-inserts')),
                ('aos_operator_access_ptr', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Pointer to Operator AOS-number')),
                ('data_jack_flags', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Datajack-flag')),
                ('onhook_alarm_delay', models.PositiveIntegerField(default=500, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Delay for on-hook card alarm delay')),
                ('post_onhook_alarm_delay', models.PositiveIntegerField(default=100, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Delay for on-hook card alarm delay after call')),
                ('card_alarm_duration', models.PositiveIntegerField(default=1000, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Duration of card-alarm')),
                ('alarm_cadence_on_timer', models.PositiveIntegerField(default=50, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Card-alarm On-cadence')),
                ('alarm_cadence_off_timer', models.PositiveIntegerField(default=50, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Card-alarm Off-cadence')),
                ('cardrdr_blocked_alarm_delay', models.PositiveIntegerField(default=300, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Delay until card-reader blocked Alarm')),
                ('settle_time', models.PositiveSmallIntegerField(default=8, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Settlement time')),
                ('grace_period_domestic', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Grace period for domestic calls')),
                ('ias_timeout', models.PositiveSmallIntegerField(default=90, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='IAS timeout')),
                ('grace_period_international', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Grace period for international calls')),
                ('settle_time_datajack', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Settlement-time for datajack-calls')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'verbose_name_plural': 'Feature Config & Call Options',
                'verbose_name': 'Feature Config & Call Options',
            },
        ),
        migrations.CreateModel(
            name='InstallParms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('access_code', models.CharField(default='2727378', help_text='For default access-code CRASERV: 2727378', max_length=7, validators=[django.core.validators.MinLengthValidator(7), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Craft-interface access code')),
                ('key_card_num', models.CharField(default='0000000000', help_text='Only for DeskSets. Keep 0000000000 for MultiPay devices.', max_length=10, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Craft-interface keycard number')),
                ('install_servicing_flags', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('01', 'Predial string enable'), ('02', 'Predial string enable for toll 1+ calls'), ('04', 'Predial string enable for intl 011+ calls'), ('08', 'Prefix prdial string to all except free calls'), ('10', 'MTR 1.x: Spare 4 / MTR 2.x: Predial string enable for primary datapac'), ('20', 'MTR 1.x: Spare 5 / MTR 2.x: Predial string enable for alternate datapac'), ('40', 'MTR 1.x: Spare 6 / MTR 2.x: AMP enable'), ('80', 'Spare 7')], max_length=23, null=True, verbose_name='Install/Servicing Flags')),
                ('tx_pkt_delay', models.PositiveSmallIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='TX Paket Delay')),
                ('rx_pkt_gap', models.PositiveSmallIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='RX Paket Gap')),
                ('coin_servicing', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('02', 'Cashbox Query Menu is Accessible')], help_text='MTR 2.x only', max_length=2, null=True, verbose_name='Coin servicing flags')),
                ('coin_box_lock_timeout', models.PositiveIntegerField(default=300, validators=[django.core.validators.MaxValueValidator(65535), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Coinbox Lock Timeout')),
                ('predial_string', models.CharField(blank=True, max_length=8, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Predial String')),
                ('alt_predial_string', models.CharField(blank=True, max_length=8, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Alternate Predial String')),
                ('analog_mode_prefix', models.CharField(blank=True, help_text='MTR 2.x only', max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Analog mode prefix for datacalls using wireless setup')),
                ('comm_saving_flags', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('01', 'Store OP-Code 996 to Upload Later with Call-in')], help_text='MTR 2.x only', max_length=2, null=True, verbose_name='Communication saving flags')),
                ('retries_till_oos', models.PositiveSmallIntegerField(blank=True, help_text='MTR 2.x only', null=True, validators=[django.core.validators.MaxValueValidator(255), django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Voice data timeout')),
                ('ds_serv_enable_flags', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('01', 'Enable CS-Serv - probably...')], help_text='MTR 2.x only', max_length=2, null=True, verbose_name='DS Serv enable flags')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'verbose_name_plural': 'Installation/Service parameters',
                'verbose_name': 'Installation/Service parameters',
            },
        ),
        migrations.CreateModel(
            name='NCCTermParms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('datapac_num', models.CharField(default='15145551111', help_text='Pay attention to provide the right number. Entering the wrong number might involving a trip to your device to put it back in service!', max_length=12, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Primary NCC number')),
                ('alt_datapac_num', models.CharField(default='15145551111', help_text='If you do not have a secondary NCC access-number, put in the same as the primary one.', max_length=12, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='Alternate NCC number')),
                ('cad_id', models.CharField(blank=True, help_text='MTR 2.x only', max_length=8, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='CAD ID')),
                ('cpe_id', models.CharField(blank=True, help_text='MTR 2.x only', max_length=8, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.', 'Invalid Number')], verbose_name='CPE ID')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'verbose_name_plural': 'NCC/terminal access parameters',
                'verbose_name': 'NCC/terminal access parameters',
            },
        ),
        migrations.AddField(
            model_name='coinvaldefs',
            name='coinValTable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='millenniumpanel.CoinValTable'),
        ),
        migrations.AlterUniqueTogether(
            name='ncctermparms',
            unique_together=set([('name', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='installparms',
            unique_together=set([('name', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='fconfigopts',
            unique_together=set([('name', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='coinvaltable',
            unique_together=set([('name', 'tenant')]),
        ),
    ]
