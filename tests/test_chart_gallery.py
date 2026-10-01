from pathlib import Path
import unittest

SITE = Path(r"C:/Users/Aornob/PowerBI-Portfolio/site/index.html")

class ChartGalleryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = SITE.read_text(encoding="utf-8")

    def test_dashboard_contains_ten_additional_chart_panels(self):
        expected = (
            'id="outcomeDonut"',
            'id="funnelChart"',
            'id="carrierStack"',
            'id="pickHistogram"',
            'id="valueScatter"',
            'id="skuTreemap"',
            'id="weekdayChart"',
            'id="otifGauge"',
            'id="monthlyArea"',
            'id="pickBoxPlot"',
        )
        for marker in expected:
            with self.subTest(marker=marker):
                self.assertIn(marker, self.html)

    def test_every_added_visual_is_refreshed_by_dashboard_render(self):
        for name in (
            "renderOutcomeDonut(data)",
            "renderFunnel(data)",
            "renderCarrierStack(data)",
            "renderPickHistogram(data)",
            "renderValueScatter(data)",
            "renderSkuTreemap(data)",
            "renderWeekdayChart(data)",
            "renderOtifGauge(data)",
            "renderMonthlyArea(data)",
            "renderPickBoxPlot(data)",
        ):
            with self.subTest(renderer=name):
                self.assertIn(name, self.html)

    def test_each_chart_has_a_direct_click_to_filter_hook(self):
        expected = (
            'data-month="${d.m}"',
            'data-funnel-stage="${i}"',
            'data-pick-bin="${i}"',
            'data-order-id="${d.OrderID}"',
            'data-weekday="${i}"',
            'data-area-service="otif"',
            'data-gauge-action="otif"',
            'chartFilters.pickBand',
            'chartFilters.weekday',
        )
        for marker in expected:
            with self.subTest(marker=marker):
                self.assertTrue(marker in self.html, f"Missing direct chart interaction: {marker}")

    def test_chart_click_dispatcher_filters_data_and_has_an_accessible_clear_action(self):
        expected = (
            'document.addEventListener(\'click\'',
            "dispatchEvent(new MouseEvent('click'",
            'data-chart-action="month"',
            'data-chart-action="pick-band"',
            'chartFilters.fullPickOnly',
            'clearChartFilters',
            'updateChartFilterStatus()',
        )
        for marker in expected:
            with self.subTest(marker=marker):
                self.assertIn(marker, self.html)

if __name__ == "__main__":
    unittest.main()
