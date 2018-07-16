import _plotly_utils.basevalidators


class ReversescaleValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self,
        plotly_name='reversescale',
        parent_name='parcoords.line',
        **kwargs
    ):
        super(ReversescaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='style',
            **kwargs
        )
