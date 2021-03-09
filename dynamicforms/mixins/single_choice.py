class SingleChoiceMixin():

    def __init__(self, *args, single_choice_supress=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.single_choice_supress = single_choice_supress

    def set_single_choice_supress(self, value):
        self._single_choice_supress = value
        if value and len(self.choices) <= 1:
            self.display_form = 'DisplayMode.SUPRESS'

    single_choice_supress = property(lambda self: self._single_choice_supress, set_single_choice_supress)
