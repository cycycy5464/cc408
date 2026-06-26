// CC408 Knowledge Graph - Enhanced with real data loading
(function() {
  'use strict';

  var container = document.getElementById('knowledge-graph');
  if (!container) return;

  var width = container.clientWidth;
  var height = container.clientHeight;

  // Subject color mapping
  var subjectColors = {
    'data-structure': '#58d6c0',
    'computer-org': '#f59e0b',
    'os': '#8b5cf6',
    'network': '#3b82f6'
  };

  var subjectNames = {
    'data-structure': '数据结构',
    'computer-org': '计算机组成原理',
    'os': '操作系统',
    'network': '计算机网络'
  };

  // Create SVG
  var svg = d3.select('#knowledge-graph')
    .append('svg')
    .attr('width', width)
    .attr('height', height);

  // Zoom behavior
  var zoom = d3.zoom()
    .scaleExtent([0.1, 4])
    .on('zoom', function(event) {
      svg.attr('transform', event.transform);
    });

  svg.call(zoom);

  var g = svg.append('g');

  // Load data
  d3.json('/data/knowledge-graph.json').then(function(data) {
    if (!data || !data.nodes.length) return;

    // Force simulation
    var simulation = d3.forceSimulation(data.nodes)
      .force('link', d3.forceLink(data.links).id(function(d) { return d.id; }).distance(120))
      .force('charge', d3.forceManyBody().strength(-300))
      .force('center', d3.forceCenter(width / 2, height / 2))
      .force('collision', d3.forceCollide().radius(40));

    // Draw links
    var link = g.selectAll('.link')
      .data(data.links)
      .enter().append('line')
      .attr('class', 'link')
      .attr('stroke', '#30363d')
      .attr('stroke-width', 1.5);

    // Draw node groups
    var node = g.selectAll('.node')
      .data(data.nodes)
      .enter().append('g')
      .attr('class', 'node')
      .call(d3.drag()
        .on('start', dragStarted)
        .on('drag', dragged)
        .on('end', dragEnded));

    // Node circles
    node.append('circle')
      .attr('r', function(d) { return 15 + (d.difficulty || 1) * 5; })
      .attr('fill', function(d) { return subjectColors[d.subject] || '#888'; })
      .attr('opacity', 0.8)
      .style('cursor', 'pointer');

    // Node labels
    node.append('text')
      .attr('dy', function(d) { return 22 + (d.difficulty || 1) * 5; })
      .attr('text-anchor', 'middle')
      .attr('fill', '#e6edf3')
      .attr('font-size', '11px')
      .text(function(d) { return d.label; });

    // Click handler
    node.on('click', function(event, d) {
      event.stopPropagation();
      showNodeInfo(d);
    });

    // Double click
    node.on('dblclick', function(event, d) {
      event.preventDefault();
      if (d.slug) {
        window.location.href = '/docs/' + d.subject + '/' + d.slug + '/';
      }
    });

    function showNodeInfo(d) {
      var panel = document.getElementById('node-info');
      var title = document.getElementById('info-title');
      var meta = document.getElementById('info-meta');
      var tags = document.getElementById('info-tags');
      var linkBtn = document.getElementById('info-link');

      title.textContent = d.label;
      title.style.color = subjectColors[d.subject] || '#888';
      meta.innerHTML = '<div>科目: ' + (subjectNames[d.subject] || d.subject) + '</div>' +
                       '<div>难度: ' + '⭐'.repeat(d.difficulty || 1) + '</div>';
      tags.innerHTML = '';
      if (d.prerequisites && d.prerequisites.length > 0) {
        tags.innerHTML = '<div style="margin-top: 0.5rem; font-size: 0.8rem; color: #8b949e;">前置知识: ' +
                          d.prerequisites.join(', ') + '</div>';
      }
      linkBtn.href = d.slug ? '/docs/' + d.subject + '/' + d.slug + '/' : '#';
      panel.style.display = 'block';
    }

    // Search
    var searchInput = document.getElementById('graph-search');
    if (searchInput) {
      searchInput.addEventListener('input', function() {
        var term = this.value.toLowerCase();
        if (!term) {
          node.attr('opacity', 1);
          link.attr('opacity', 1);
          return;
        }
        node.attr('opacity', function(d) {
          return d.label.toLowerCase().indexOf(term) !== -1 ? 1 : 0.15;
        });
        link.attr('opacity', 0.1);
      });
    }

    svg.on('click', function() {
      document.getElementById('node-info').style.display = 'none';
    });

    simulation.on('tick', function() {
      link
        .attr('x1', function(d) { return d.source.x; })
        .attr('y1', function(d) { return d.source.y; })
        .attr('x2', function(d) { return d.target.x; })
        .attr('y2', function(d) { return d.target.y; });

      node.attr('transform', function(d) {
        return 'translate(' + d.x + ',' + d.y + ')';
      });
    });

    function dragStarted(event, d) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }

    function dragged(event, d) {
      d.fx = event.x;
      d.fy = event.y;
    }

    function dragEnded(event, d) {
      if (!event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    }
  }).catch(function(err) {
    // Show error message in graph container
    var container = document.getElementById('knowledge-graph');
    if (container) {
      container.innerHTML = '<div style="text-align:center;padding:4rem;color:#8b949e;">知识图谱数据加载失败，请稍后重试</div>';
    }
    console.warn('Knowledge graph data load error:', err);
  });
})();
