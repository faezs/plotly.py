import _plotly_utils.basevalidators


class FamilyValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='family',
        parent_name='layout.updatemenu.font',
        **kwargs
    ):
        super(FamilyValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='arraydraw',
            no_blank=True,
            role='style',
            strict=True,
            **kwargs
        )
