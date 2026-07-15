// charts.js - Geopolitical Economic Outlook 2026-2027
(function() {
  var style = getComputedStyle(document.documentElement);
  var accent = style.getPropertyValue('--accent').trim();
  var accent2 = style.getPropertyValue('--accent2').trim();
  var ink = style.getPropertyValue('--ink').trim();
  var muted = style.getPropertyValue('--muted').trim();
  var rule = style.getPropertyValue('--rule').trim();
  var bg2 = style.getPropertyValue('--bg2').trim();
  var green = style.getPropertyValue('--green').trim();
  var red = style.getPropertyValue('--red').trim();
  var orange = style.getPropertyValue('--orange').trim();

  // --- Chart 1: Oil Price & Inflation Scenarios ---
  var chart1 = echarts.init(document.getElementById('chart-oil-inflation'), null, { renderer: 'svg' });
  chart1.setOption({
    tooltip: { trigger: 'axis', appendToBody: true },
    legend: {
      data: ['布伦特原油 ($/桶)', '全球通胀率 (%)'],
      textStyle: { color: muted },
      top: 0
    },
    grid: { left: 60, right: 40, top: 40, bottom: 40 },
    xAxis: {
      type: 'category',
      data: ['2026 Q1', '2026 Q2', '2026 Q3\n(当前)', '2026 Q4', '2027 Q1\n(夺岛窗口)', '2027 Q2', '2027 Q3'],
      axisLine: { lineStyle: { color: rule } },
      axisLabel: { color: muted, fontSize: 11 },
      splitLine: { show: false }
    },
    yAxis: [
      { type: 'value', name: '美元/桶', nameTextStyle: { color: muted, fontSize: 11 }, min: 40, max: 160, axisLine: { show: false }, axisLabel: { color: muted }, splitLine: { lineStyle: { color: rule, type: 'dashed' } } },
      { type: 'value', name: '%', nameTextStyle: { color: muted, fontSize: 11 }, min: 0, max: 12, axisLine: { show: false }, axisLabel: { color: muted }, splitLine: { show: false } }
    ],
    series: [
      {
        name: '布伦特原油 ($/桶)',
        type: 'line',
        data: [72, 68, 79, { value: 95, symbol: 'emptyCircle', symbolSize: 12, itemStyle: { color: orange } }, { value: 110, symbol: 'emptyCircle', symbolSize: 12, itemStyle: { color: red } }, 90, 85],
        smooth: true,
        lineStyle: { color: accent, width: 3 },
        itemStyle: { color: accent },
        areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{ offset: 0, color: accent + '33' }, { offset: 1, color: accent + '05' }] } },
        markLine: {
          silent: true,
          data: [
            { yAxis: 100, label: { formatter: '警戒线 $100', color: red, fontSize: 10 }, lineStyle: { color: red, type: 'dashed' } },
            { yAxis: 150, label: { formatter: '危机线 $150', color: red, fontSize: 10 }, lineStyle: { color: red, type: 'dashed', width: 2 } }
          ]
        },
        z: 2
      },
      {
        name: '全球通胀率 (%)',
        type: 'line',
        yAxisIndex: 1,
        data: [3.5, 3.2, 4.1, { value: 5.5, symbol: 'emptyCircle', symbolSize: 12, itemStyle: { color: orange } }, { value: 7.5, symbol: 'emptyCircle', symbolSize: 12, itemStyle: { color: red } }, 6.0, 5.0],
        smooth: true,
        lineStyle: { color: accent2, width: 3, type: 'dashed' },
        itemStyle: { color: accent2 },
        z: 1
      }
    ],
    animation: false
  });
  window.addEventListener('resize', function() { chart1.resize(); });

  // --- Chart 2: Island Seizure Probability Assessment ---
  var chart2 = echarts.init(document.getElementById('chart-prob'), null, { renderer: 'svg' });
  chart2.setOption({
    tooltip: { trigger: 'axis', appendToBody: true },
    legend: {
      data: ['军事可行性', '政治意愿', '国际反应'],
      textStyle: { color: muted }
    },
    grid: { left: 50, right: 40, top: 40, bottom: 40 },
    radar: {
      indicator: [
        { name: '特种突袭\n(无占领)', max: 100 },
        { name: '有限夺岛\n(短期控制)', max: 100 },
        { name: '大规模夺岛\n(长期占领)', max: 100 },
        { name: '不发生\n夺岛行动', max: 100 }
      ],
      radius: '60%',
      axisName: { color: muted, fontSize: 11 },
      splitArea: { areaStyle: { color: [bg2 + '55', bg2 + '33'] } },
      axisLine: { lineStyle: { color: rule } }
    },
    series: [{
      type: 'radar',
      data: [
        { value: [85, 40, 15, 65], name: '军事可行性', lineStyle: { color: accent, width: 2 }, areaStyle: { color: accent + '22' }, itemStyle: { color: accent } },
        { value: [70, 35, 10, 55], name: '政治意愿', lineStyle: { color: accent2, width: 2 }, areaStyle: { color: accent2 + '22' }, itemStyle: { color: accent2 } },
        { value: [15, 10, 5, 85], name: '国际反应', lineStyle: { color: orange, width: 2 }, areaStyle: { color: orange + '22' }, itemStyle: { color: orange } }
      ]
    }],
    animation: false
  });
  window.addEventListener('resize', function() { chart2.resize(); });

  // --- Chart 3: Three Scenarios Economic Comparison ---
  var chart3 = echarts.init(document.getElementById('chart-scenario'), null, { renderer: 'svg' });
  chart3.setOption({
    tooltip: {
      trigger: 'axis',
      appendToBody: true,
      formatter: function(params) {
        var res = '<strong>' + params[0].axisValue + '</strong><br/>';
        params.forEach(function(p) {
          res += '<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:' + p.color + ';margin-right:6px;"></span>' + p.seriesName + ': ';
          if (p.seriesName === '全球通胀率 (%)' || p.seriesName === '全球GDP增速 (%)') {
            res += p.value + '%';
          } else {
            res += '$' + p.value;
          }
          res += '<br/>';
        });
        return res;
      }
    },
    legend: {
      data: ['布伦特原油 ($/桶)', '全球通胀率 (%)', '全球GDP增速 (%)'],
      textStyle: { color: muted }
    },
    grid: { left: 60, right: 40, top: 60, bottom: 40 },
    xAxis: {
      type: 'category',
      data: ['基准情景\n(~55%)', '紧张升级\n(~30%)', '全面冲突\n(~15%)'],
      axisLine: { lineStyle: { color: rule } },
      axisLabel: { color: ink, fontSize: 12, fontWeight: 'bold' },
      splitLine: { show: false }
    },
    yAxis: [
      { type: 'value', name: '美元/桶', nameTextStyle: { color: muted, fontSize: 11 }, min: 0, max: 220, axisLine: { show: false }, axisLabel: { color: muted }, splitLine: { lineStyle: { color: rule, type: 'dashed' } } },
      { type: 'value', name: '%', nameTextStyle: { color: muted, fontSize: 11 }, min: -5, max: 12, axisLine: { show: false }, axisLabel: { color: muted }, splitLine: { show: false } }
    ],
    series: [
      {
        name: '布伦特原油 ($/桶)',
        type: 'bar',
        data: [
          { value: 90, itemStyle: { color: green } },
          { value: 135, itemStyle: { color: orange } },
          { value: 175, itemStyle: { color: red } }
        ],
        barWidth: '25%',
        label: { show: true, position: 'top', color: ink, fontSize: 13, fontWeight: 'bold', formatter: function(p) { return '$' + p.value; } }
      },
      {
        name: '全球通胀率 (%)',
        type: 'bar',
        yAxisIndex: 1,
        data: [
          { value: 4.0, itemStyle: { color: green + 'cc' } },
          { value: 7.0, itemStyle: { color: orange + 'cc' } },
          { value: 10.0, itemStyle: { color: red + 'cc' } }
        ],
        barWidth: '25%',
        label: { show: true, position: 'top', color: ink, fontSize: 13, fontWeight: 'bold', formatter: function(p) { return p.value + '%'; } }
      },
      {
        name: '全球GDP增速 (%)',
        type: 'line',
        yAxisIndex: 1,
        data: [2.0, 0.5, -2.0],
        smooth: false,
        lineStyle: { color: accent, width: 3 },
        itemStyle: { color: accent },
        symbolSize: 12,
        label: { show: true, position: 'bottom', color: ink, fontSize: 13, fontWeight: 'bold', formatter: function(p) { return p.value + '%'; } },
        z: 3
      }
    ],
    animation: false
  });
  window.addEventListener('resize', function() { chart3.resize(); });

})();
