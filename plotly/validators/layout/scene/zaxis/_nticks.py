import _plotly_utils.basevalidators


class NticksValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self, plotly_name='nticks', parent_name='layout.scene.zaxis', **kwargs
    ):
        super(NticksValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            min=0,
            role='style',
            **kwargs
        )
