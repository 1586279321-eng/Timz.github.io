/**
 * 侧边栏折叠/展开功能
 */
document.addEventListener('DOMContentLoaded', function () {
  const sidebar = document.getElementById('sidebar');
  const toggleBtn = document.getElementById('sidebar-collapse-btn');

  if (!sidebar || !toggleBtn) {
    return;
  }

  // 恢复折叠状态
  const collapsed = localStorage.getItem('sidebar-collapsed') === 'true';
  if (collapsed) {
    sidebar.classList.add('collapsed');
  }

  // 点击按钮切换
  toggleBtn.addEventListener('click', function () {
    sidebar.classList.toggle('collapsed');
    const isCollapsed = sidebar.classList.contains('collapsed');
    localStorage.setItem('sidebar-collapsed', isCollapsed.toString());
  });
});
