from django import forms
from .models import Choice, Question

class SurveyForm(forms.Form):
	# abortion_CHOICES = (
	# 	('1', 'Strongly Disagree'),
	# 	('2', 'Disagree'),
	# 	('3', 'Neutral'),
	# 	('4', 'Agree'),
	# 	('5', 'Strongly Agree'),
	# 	)
	# hiring_CHOICES = (
	# 	('6', 'Strongly Disagree'),
	# 	('7', 'Disagree'),
	# 	('8', 'Neutral'),
	# 	('9', 'Agree'),
	# 	('10', 'Strongly Agree'),
	# 	)
	# marriage_CHOICES = (
	# 	('11', 'Strongly Disagree'),
	# 	('12', 'Disagree'),
	# 	('13', 'Neutral'),
	# 	('14', 'Agree'),
	# 	('15', 'Strongly Agree'),
	# 	)
	# god_CHOICES = (
	# 	('16', 'Strongly Disagree'),
	# 	('17', 'Disagree'),
	# 	('18', 'Neutral'),
	# 	('19', 'Agree'),
	# 	('20', 'Strongly Agree'),
	# 	)
	# obamacare_CHOICES = (
	# 	('21', 'Strongly Disagree'),
	# 	('22', 'Disagree'),
	# 	('23', 'Neutral'),
	# 	('24', 'Agree'),
	# 	('25', 'Strongly Agree'),
	# 	)
	# socialsec_CHOICES = (
	# 	('26', 'Strongly Disagree'),
	# 	('27', 'Disagree'),
	# 	('28', 'Neutral'),
	# 	('29', 'Agree'),
	# 	('30', 'Strongly Agree'),
	# 	)
	# vouchers_CHOICES = (
	# 	('31', 'Strongly Disagree'),
	# 	('32', 'Disagree'),
	# 	('33', 'Neutral'),
	# 	('34', 'Agree'),
	# 	('35', 'Strongly Agree'),
	# 	)
	# pollution_CHOICES = (
	# 	('36', 'Strongly Disagree'),
	# 	('37', 'Disagree'),
	# 	('38', 'Neutral'),
	# 	('39', 'Agree'),
	# 	('40', 'Strongly Agree'),
	# 	)
	# punishment_CHOICES = (
	# 	('41', 'Strongly Disagree'),
	# 	('42', 'Disagree'),
	# 	('43', 'Neutral'),
	# 	('44', 'Agree'),
	# 	('45', 'Strongly Agree'),
	# 	)
	# gun_CHOICES = (
	# 	('46', 'Strongly Disagree'),
	# 	('47', 'Disagree'),
	# 	('48', 'Neutral'),
	# 	('49', 'Agree'),
	# 	('50', 'Strongly Agree'),
	# 	)
	# tax_CHOICES = (
	# 	('51', 'Strongly Disagree'),
	# 	('52', 'Disagree'),
	# 	('53', 'Neutral'),
	# 	('54', 'Agree'),
	# 	('55', 'Strongly Agree'),
	# 	)
	# pathway_CHOICES = (
	# 	('56', 'Strongly Disagree'),
	# 	('57', 'Disagree'),
	# 	('58', 'Neutral'),
	# 	('59', 'Agree'),
	# 	('60', 'Strongly Agree'),
	# 	)
	# trade_CHOICES = (
	# 	('61', 'Strongly Disagree'),
	# 	('62', 'Disagree'),
	# 	('63', 'Neutral'),
	# 	('64', 'Agree'),
	# 	('65', 'Strongly Agree'),
	# 	)
	# exceptionalism_CHOICES = (
	# 	('66', 'Strongly Disagree'),
	# 	('67', 'Disagree'),
	# 	('68', 'Neutral'),
	# 	('69', 'Agree'),
	# 	('70', 'Strongly Agree'),
	# 	)
	# military_CHOICES = (
	# 	('71', 'Strongly Disagree'),
	# 	('72', 'Disagree'),
	# 	('73', 'Neutral'),
	# 	('74', 'Agree'),
	# 	('75', 'Strongly Agree'),
	# 	)
	# registration_CHOICES = (
	# 	('76', 'Strongly Disagree'),
	# 	('77', 'Disagree'),
	# 	('78', 'Neutral'),
	# 	('79', 'Agree'),
	# 	('80', 'Strongly Agree'),
	# 	)
	# foreign_CHOICES = (
	# 	('81', 'Strongly Disagree'),
	# 	('82', 'Disagree'),
	# 	('83', 'Neutral'),
	# 	('84', 'Agree'),
	# 	('85', 'Strongly Agree'),
	# 	)
	# green_CHOICES = (
	# 	('86', 'Strongly Disagree'),
	# 	('87', 'Disagree'),
	# 	('88', 'Neutral'),
	# 	('89', 'Agree'),
	# 	('90', 'Strongly Agree'),
	# 	)
	# marijuana_CHOICES = (
	# 	('91', 'Strongly Disagree'),
	# 	('92', 'Disagree'),
	# 	('93', 'Neutral'),
	# 	('94', 'Agree'),
	# 	('95', 'Strongly Agree'),
	# 	)
	# stimulus_CHOICES = (
	# 	('96', 'Strongly Disagree'),
	# 	('97', 'Disagree'),
	# 	('98', 'Neutral'),
	# 	('99', 'Agree'),
	# 	('100', 'Strongly Agree'),
	# 	)
	# abortion_select = forms.ChoiceField(choices=abortion_CHOICES, widget=forms.RadioSelect, label = 'Abortion is a woman\'s unrestricted right')
	# hiring_select = forms.ChoiceField(choices=hiring_CHOICES, widget=forms.RadioSelect, label = 'Legally require hiring more women & minorities')
	# marriage_select = forms.ChoiceField(choices=marriage_CHOICES, widget=forms.RadioSelect, label = 'Comfortable with same-sex marriage')
	# god_select = forms.ChoiceField(choices=god_CHOICES, widget=forms.RadioSelect, label = 'Keep God in the public sphere')
	# obamacare_select = forms.ChoiceField(choices=obamacare_CHOICES, widget=forms.RadioSelect, label = 'Expand ObamaCare')
	# socialsec_select = forms.ChoiceField(choices=socialsec_CHOICES, widget=forms.RadioSelect, label = 'Privatize Social Security')
	# vouchers_select = forms.ChoiceField(choices=vouchers_CHOICES, widget=forms.RadioSelect, label = 'Vouchers for school choice')
	# pollution_select = forms.ChoiceField(choices=pollution_CHOICES, widget=forms.RadioSelect, label = 'Society bears cost of pollution')
	# punishment_select = forms.ChoiceField(choices=punishment_CHOICES, widget=forms.RadioSelect, label = 'Stricter punishment reduces crime')
	# gun_select = forms.ChoiceField(choices=gun_CHOICES, widget=forms.RadioSelect, label = 'Absolute right to gun ownership')
	# tax_select = forms.ChoiceField(choices=tax_CHOICES, widget=forms.RadioSelect, label = 'Higher taxes on the wealthy')
	# pathway_select = forms.ChoiceField(choices=pathway_CHOICES, widget=forms.RadioSelect, label = 'Pathway to citizenship for illegal aliens')
	# trade_select = forms.ChoiceField(choices=trade_CHOICES, widget=forms.RadioSelect, label = 'Support & expand free trade')
	# exceptionalism_select = forms.ChoiceField(choices=exceptionalism_CHOICES, widget=forms.RadioSelect, label = 'Support American Exceptionalism')
	# military_select = forms.ChoiceField(choices=military_CHOICES, widget=forms.RadioSelect, label = 'Expand the military')
	# registration_select = forms.ChoiceField(choices=registration_CHOICES, widget=forms.RadioSelect, label = 'Make voter registration easier')
	# foreign_select = forms.ChoiceField(choices=foreign_CHOICES, widget=forms.RadioSelect, label = 'Avoid foreign entanglements')
	# green_select = forms.ChoiceField(choices=green_CHOICES, widget=forms.RadioSelect, label = 'Prioritize green energy')
	# marijuana_select = forms.ChoiceField(choices=marijuana_CHOICES, widget=forms.RadioSelect, label = 'Marijuana is a gateway drug')
	# stimulus_select = forms.ChoiceField(choices=stimulus_CHOICES, widget=forms.RadioSelect, label = 'Stimulus better than market-led recovery')
	
	


	CHOICES_POSITIVE = (
		('-5', 'Strongly Disagree'),
		('-2.5', 'Disagree'),
		('0', 'Neutral'),
		('2.5', 'Agree'),
		('5', 'Strongly Agree'),
		)


	CHOICES_NEGATIVE = (
		('5', 'Strongly Disagree'),
		('2.5', 'Disagree'),
		('0', 'Neutral'),
		('-2.5', 'Agree'),
		('-5', 'Strongly Agree'),
		)


	abortion_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Abortion is a woman\'s unrestricted right')
	hiring_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Legally require hiring more women & minorities')
	marriage_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Comfortable with same-sex marriage')
	god_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'Keep God in the public sphere')
	obamacare_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Expand ObamaCare')
	socialsec_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'Privatize Social Security')
	vouchers_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'Vouchers for school choice')
	pollution_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'Society bears cost of pollution')
	punishment_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'Stricter punishment reduces crime')
	gun_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'Absolute right to gun ownership')
	tax_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Higher taxes on the wealthy')
	pathway_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Pathway to citizenship for illegal aliens')
	trade_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'Support & expand free trade')
	exceptionalism_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'Support American Exceptionalism')
	military_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'Expand the military')
	registration_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Make voter registration easier')
	foreign_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Avoid foreign entanglements')
	green_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Prioritize green energy')
	marijuana_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'Marijuana is a gateway drug')
	stimulus_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Stimulus better than market-led recovery')
	
	
