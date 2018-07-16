import _plotly_utils.basevalidators


class BorderpadValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='borderpad',
        parent_name='layout.scene.annotation',
        **kwargs
    ):
        super(BorderpadValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            min=0,
            role='style',
            **kwargs
        )
