import _plotly_utils.basevalidators


class ShowgridValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self, plotly_name='showgrid', parent_name='layout.yaxis', **kwargs
    ):
        super(ShowgridValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='ticks',
            role='style',
            **kwargs
        )
