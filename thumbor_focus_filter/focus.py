#!/usr/bin/env python
# -*- coding: utf-8 -*-

from thumbor.filters import BaseFilter, filter_method
from thumbor.point import FocalPoint


class Filter(BaseFilter):
    @filter_method(
        BaseFilter.PositiveNumber,#percentage_width
        BaseFilter.PositiveNumber,#percentage_height
    )
    def text(self, percentage_width, percentage_height):
        source_width, source_height = self.context.request.engine.size
        
        left = (percentage_width / 100) * source_width
        top = (percentage_height / 100) * source_height
        width = source_width
        height = source_height
            
        self.context.request.focal_points.append(
            FocalPoint.from_square(left, top, width, height, origin="Explicit")
        )