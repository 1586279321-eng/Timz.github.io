/**
 * 左侧目录侧边栏的折叠/展开功能
 */
document.addEventListener('DOMContentLoaded', function () {
  const sidebar = document.getElementById('toc-left-sidebar');
  const toggleBtn = document.getElementById('toc-left-toggle');

  if (!sidebar || !toggleBtn) {
    return;
  }

  // 从 localStorage 读取折叠状态
  const collapsed = localStorage.getItem('toc-left-collapsed') === 'true';
  if (collapsed) {
    sidebar.classList.add('collapsed');
  }

  // 点击按钮切换折叠
  toggleBtn.addEventListener('click', function () {
    sidebar.classList.toggle('collapsed');
    const isCollapsed = sidebar.classList.contains('collapsed');
    localStorage.setItem('toc-left-collapsed', isCollapsed.toString());
  });
});
