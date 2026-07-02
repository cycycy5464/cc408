// CC408 Knowledge Graph - Inline data from Hugo partial
(function() {
  'use strict';

  var container = document.getElementById('knowledge-graph');
  if (!container) return;
  var width = container.clientWidth;
  var height = container.clientHeight;

  var subjectColors = {
    'data-structure': '#58d6c0', 'computer-org': '#f59e0b',
    'os': '#8b5cf6', 'network': '#3b82f6'
  };
  var subjectNames = {
    'data-structure': '数据结构', 'computer-org': '计算机组成原理',
    'os': '操作系统', 'network': '计算机网络'
  };

  // Inline data
  var data;
  try {
    data = window.__GRAPH_DATA__;
  } catch(e) {
    console.error('Knowledge graph data error:', e);
    container.innerHTML = '<p style="color:var(--color-co);padding:2rem;text-align:center">图谱数据加载失败</p>';
    return;
  }
  if (!data || !data.nodes || !data.nodes.length) return;

  var svg = d3.select('#knowledge-graph').append('svg').attr('width', width).attr('height', height);
  var zoom = d3.zoom().scaleExtent([0.1, 4]).on('zoom', function(e) { g.attr('transform', e.transform); });
  svg.call(zoom);
  var g = svg.append('g');

  var simulation = d3.forceSimulation(data.nodes)
    .force('link', d3.forceLink(data.links).id(function(d) { return d.id; }).distance(100))
    .force('charge', d3.forceManyBody().strength(-250))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collision', d3.forceCollide().radius(35));

  var link = g.selectAll('.link').data(data.links).enter().append('line')
    .attr('stroke', '#30363d').attr('stroke-width', 1.5).attr('opacity', 0.6);

  var node = g.selectAll('.node').data(data.nodes).enter().append('g')
    .attr('class', 'node').call(d3.drag().on('start', function(e, d) {
      if (!e.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x; d.fy = d.y;
    }).on('drag', function(e, d) { d.fx = e.x; d.fy = e.y; })
      .on('end', function(e, d) { if (!e.active) simulation.alphaTarget(0); d.fx = null; d.fy = null; }));

  node.append('circle').attr('r', function(d) { return 12 + (d.difficulty || 1) * 4; })
    .attr('fill', function(d) { return subjectColors[d.subject] || '#888'; }).attr('opacity', 0.85).style('cursor', 'pointer');

  node.append('text').attr('dy', '0.35em').attr('text-anchor', 'middle')
    .attr('fill', '#e6edf3').attr('font-size', '9px').style('pointer-events', 'none')
    .text(function(d) { return d.label; });

  node.on('click', function(e, d) {
    // On mobile, navigate directly. On desktop, show info panel.
    if (window.innerWidth <= 768) {
      window.location.href = d.id;
      return;
    }
    e.stopPropagation();
    document.getElementById('info-title').textContent = d.label;
    document.getElementById('info-title').style.color = subjectColors[d.subject] || '#888';
    document.getElementById('info-meta').innerHTML =
      '科目: ' + (subjectNames[d.subject] || d.subject) + '<br>难度: ' + '&#9733;'.repeat(d.difficulty || 1);
    document.getElementById('info-tags').innerHTML = d.prerequisites && d.prerequisites.length ?
      '<div style="font-size:0.8rem;color:#8b949e;">前置: ' + d.prerequisites.join(', ') + '</div>' : '';
    // Build correct link
    document.getElementById('info-link').href = d.id;
    document.getElementById('node-info').style.display = 'block';
  });

  node.on('dblclick', function(e, d) {
    window.location.href = d.id;
  });

  svg.on('click', function() { document.getElementById('node-info').style.display = 'none'; });

  // Search
  var searchInput = document.getElementById('graph-search');
  if (searchInput) searchInput.addEventListener('input', function() {
    var t = this.value.toLowerCase();
    node.attr('opacity', function(d) { return !t || d.label.toLowerCase().indexOf(t) !== -1 ? 1 : 0.15; });
    link.attr('opacity', t ? 0.05 : 0.6);
  });

  simulation.on('tick', function() {
    link.attr('x1', function(d) { return d.source.x; }).attr('y1', function(d) { return d.source.y; })
      .attr('x2', function(d) { return d.target.x; }).attr('y2', function(d) { return d.target.y; });
    node.attr('transform', function(d) { return 'translate(' + d.x + ',' + d.y + ')'; });
  });
})();
