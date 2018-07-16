import _plotly_utils.basevalidators


class TicktextValidator(_plotly_utils.basevalidators.DataArrayValidator):

    def __init__(
        self, plotly_name='ticktext', parent_name='layout.xaxis', **kwargs
    ):
        super(TicktextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='ticks+margins',
            role='data',
            **kwargs
        )
