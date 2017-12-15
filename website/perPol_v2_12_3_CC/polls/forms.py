from django import forms

class SurveyForm(forms.Form):

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

	us_states=(
		'Alabama',
		'Alaska',
		'Arizona',
		'Arkansas',
		'California',
		'Colorado',
		'Connecticut',
		'Delaware',
		'Florida',
		'Georgia',
		'Hawaii',
		'Idaho',
		'Illinois',
		'Indiana',
		'Iowa',
		'Kansas',
		'Kentucky',
		'Louisiana',
		'Maine',
		'Maryland',
		'Massachusetts',
		'Michigan',
		'Minnesota',
		'Mississippi',
		'Missouri',
		'Montana',
		'Nebraska',
		'Nevada',
		'New Hampshire',
		'New Jersey',
		'New Mexico',
		'New York',
		'North Carolina',
		'North Dakota',
		'Ohio',
		'Oklahoma',
		'Oregon',
		'Pennsylvania',
		'Rhode Island',
		'South Carolina',
		'South Dakota',
		'Tennessee',
		'Texas',
		'Utah',
		'Vermont',
		'Virginia',
		'Washington',
		'West Virginia',
		'Wisconsin',
		'Wyoming',
		)

	abortion_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Abortion is a woman\'s unrestricted right')
	hiring_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Legally require hiring more women & minorities')
	marriage_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Comfortable with same-sex marriage')
	god_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'Keep God in the public sphere')
	obamacare_select = forms.ChoiceField(choices=CHOICES_NEGATIVE, widget=forms.RadioSelect, label = 'Expand ObamaCare')
	socialsec_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'Privatize Social Security')
	vouchers_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'Vouchers for school choice')
	pollution_select = forms.ChoiceField(choices=CHOICES_POSITIVE, widget=forms.RadioSelect, label = 'EPA regulations are too restrictive')
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
	state_select = forms.ChoiceField(choices=((x,x) for x in us_states), label = 'Select your state')