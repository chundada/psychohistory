(function() {
  var style = getComputedStyle(document.documentElement);
  var accent = style.getPropertyValue('--accent').trim() || '#7c3aed';
  var accent2 = style.getPropertyValue('--accent2').trim() || '#0ea5e9';
  var ink = style.getPropertyValue('--ink').trim() || '#1a1a2e';
  var muted = style.getPropertyValue('--muted').trim() || '#6b7280';
  var rule = style.getPropertyValue('--rule').trim() || '#e5e7eb';
  var bg2 = style.getPropertyValue('--bg2').trim() || '#ffffff';
  var bg = style.getPropertyValue('--bg').trim() || '#fafafa';
  var danger = '#ef4444';
  var warning = '#f59e0b';
  var success = '#22c55e';

  // --- Chart: Historical Oil Price Comparison ---
  var oilChartEl = document.getElementById('chart-oil-history');
  if (oilChartEl) {
    var oilChart = echarts.init(oilChartEl, null, { renderer: 'svg' });
    oilChart.setOption({
      animation: false,
      tooltip: { trigger: 'axis', appendToBody: true },
      legend: {
        data: ['1973年油价', '2026年油价'],
        textStyle: { color: muted, fontSize: 12 },
        top: 0
      },
      grid: { left: '10%', right: '5%', bottom: '15%', top: '18%' },
      xAxis: {
        type: 'category',
        data: ['危机前', '危机后6个月', '危机后1年', '危机后2年'],
        axisLabel: { color: muted, fontSize: 11 },
        axisLine: { lineStyle: { color: rule } }
      },
      yAxis: {
        type: 'value',
        name: '美元/桶',
        nameTextStyle: { color: muted, fontSize: 11 },
        axisLabel: { color: muted, fontSize: 11 },
        splitLine: { lineStyle: { color: rule } }
      },
      series: [
        {
          name: '1973年油价',
          type: 'line',
          data: [1.8, 5.12, 11.65, 13.5],
          smooth: true,
          lineStyle: { width: 3, color: accent },
          itemStyle: { color: accent },
          areaStyle: {
            color: {
              type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
              colorStops: [
                { offset: 0, color: accent + '30' },
                { offset: 1, color: accent + '05' }
              ]
            }
          }
        },
        {
          name: '2026年油价',
          type: 'line',
          data: [73.91, 78.51, null, null],
          smooth: true,
          lineStyle: { width: 3, color: warning },
          itemStyle: { color: warning },
          areaStyle: {
            color: {
              type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
              colorStops: [
                { offset: 0, color: warning + '30' },
                { offset: 1, color: warning + '05' }
              ]
            }
          }
        }
      ]
    });
    window.addEventListener('resize', function() { oilChart.resize(); });
  }

  // --- Chart: Global South Dedollarization Stats ---
  var dedollarChartEl = document.getElementById('chart-dedollarization');
  if (dedollarChartEl) {
    var dedollarChart = echarts.init(dedollarChartEl, null, { renderer: 'svg' });
    dedollarChart.setOption({
      animation: false,
      tooltip: { trigger: 'item', appendToBody: true },
      legend: {
        orient: 'vertical',
        right: '5%',
        top: 'center',
        textStyle: { color: muted, fontSize: 12 }
      },
      series: [
        {
          name: '本币结算占比',
          type: 'pie',
          radius: ['40%', '70%'],
          center: ['35%', '50%'],
          avoidLabelOverlap: false,
          itemStyle: {
            borderRadius: 6,
            borderColor: bg2,
            borderWidth: 2
          },
          label: { show: false },
          emphasis: {
            label: { show: true, fontSize: 14, fontWeight: 'bold' }
          },
          labelLine: { show: false },
          data: [
            { value: 95, name: '中俄贸易本币结算', itemStyle: { color: accent } },
            { value: 51, name: '沙特对华原油人民币结算', itemStyle: { color: accent2 } },
            { value: 40, name: '金砖国家GDP全球占比', itemStyle: { color: warning } }
          ]
        }
      ]
    });
    window.addEventListener('resize', function() { dedollarChart.resize(); });
  }

  // --- Chart: Eschatology Convergence ---
  var eschatologyChartEl = document.getElementById('chart-eschatology');
  if (eschatologyChartEl) {
    var eschatologyChart = echarts.init(eschatologyChartEl, null, { renderer: 'svg' });
    eschatologyChart.setOption({
      animation: false,
      tooltip: { appendToBody: true },
      radar: {
        indicator: [
          { name: '中东大战', max: 10 },
          { name: '第三圣殿', max: 10 },
          { name: '歌革玛各', max: 10 },
          { name: '敌基督现身', max: 10 },
          { name: '弥赛亚降临', max: 10 },
          { name: '最后审判', max: 10 },
          { name: '新世界秩序', max: 10 }
        ],
        center: ['50%', '50%'],
        radius: '65%',
        axisName: {
          color: muted,
          fontSize: 11
        },
        splitArea: {
          areaStyle: {
            color: [bg, bg2]
          }
        },
        axisLine: { lineStyle: { color: rule } },
        splitLine: { lineStyle: { color: rule } }
      },
      series: [{
        type: 'radar',
        data: [
          {
            value: [10, 8, 7, 5, 9, 6, 4],
            name: '犹太教',
            lineStyle: { color: danger, width: 2 },
            areaStyle: { color: danger + '20' },
            itemStyle: { color: danger }
          },
          {
            value: [9, 10, 10, 10, 9, 10, 8],
            name: '基督教锡安主义',
            lineStyle: { color: accent2, width: 2 },
            areaStyle: { color: accent2 + '20' },
            itemStyle: { color: accent2 }
          },
          {
            value: [8, 6, 7, 10, 9, 8, 5],
            name: '什叶派伊斯兰',
            lineStyle: { color: success, width: 2 },
            areaStyle: { color: success + '20' },
            itemStyle: { color: success }
          }
        ]
      }],
      legend: {
        bottom: 0,
        textStyle: { color: muted, fontSize: 12 }
      }
    });
    window.addEventListener('resize', function() { eschatologyChart.resize(); });
  }

  // --- Chart: War Escalation Levels ---
  var escalationChartEl = document.getElementById('chart-escalation');
  if (escalationChartEl) {
    var escalationChart = echarts.init(escalationChartEl, null, { renderer: 'svg' });
    escalationChart.setOption({
      animation: false,
      tooltip: { trigger: 'axis', appendToBody: true, axisPointer: { type: 'shadow' } },
      grid: { left: '3%', right: '8%', bottom: '3%', top: '10%', containLabel: true },
      xAxis: {
        type: 'value',
        name: '油价（美元/桶）',
        nameTextStyle: { color: muted, fontSize: 11 },
        axisLabel: { color: muted, fontSize: 11 },
        splitLine: { lineStyle: { color: rule } }
      },
      yAxis: {
        type: 'category',
        data: ['第四级：系统性崩溃', '第三级：地区供应链断裂', '第二级：实质性阻断', '第一级：象征性封锁'],
        axisLabel: { color: muted, fontSize: 11 },
        axisLine: { lineStyle: { color: rule } }
      },
      series: [
        {
          type: 'bar',
          data: [
            { value: 250, itemStyle: { color: danger } },
            { value: 175, itemStyle: { color: warning } },
            { value: 135, itemStyle: { color: accent2 } },
            { value: 78, itemStyle: { color: success } }
          ],
          barWidth: '60%',
          label: {
            show: true,
            position: 'right',
            formatter: '${c}',
            color: ink,
            fontSize: 12,
            fontWeight: 600
          }
        }
      ]
    });
    window.addEventListener('resize', function() { escalationChart.resize(); });
  }

})();
