import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, AutoMinorLocator, FuncFormatter



# ============================================================
# 1. ПОДГОТОВКА ДАННЫХ
# ============================================================
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# ============================================================
# 2. СОЗДАНИЕ ФИГУРЫ И ОСЕЙ
# ============================================================
fig, ax = plt.subplots(
    figsize=(10, 6),        # Размер фигуры в дюймах (ширина, высота)
    dpi=100,                # Разрешение: точек на дюйм
    facecolor='white',      # Цвет фона всей фигуры
    edgecolor='none',       # Цвет рамки фигуры
    linewidth=1,            # Толщина рамки фигуры
    frameon=True,           # Рисовать ли рамку вокруг фигуры
    layout='constrained',   # Автоматическая компоновка
)

# ============================================================
# 3. ПОСТРОЕНИЕ ДАННЫХ
# ============================================================
line1, = ax.plot(x, y1, label='sin(x)', color='steelblue', linewidth=2)
line2, = ax.plot(x, y2, label='cos(x)', color='crimson', linewidth=2, linestyle='--')

# ============================================================
# 4. ЗАГОЛОВОК И ПОДПИСИ ОСЕЙ
# ============================================================
ax.set_title(
    'Заголовок',                    # Текст заголовка
    fontsize=16,                    # Размер шрифта
    fontweight='bold',              # Насыщенность: 'normal', 'bold', 'light'
    fontstyle='normal',             # Стиль: 'normal', 'italic', 'oblique'
    fontfamily='serif',             # Семейство: 'serif', 'sans-serif', 'monospace'
    color='darkblue',               # Цвет текста
    loc='center',                   # 'left', 'center', 'right'
    pad=20,                         # Отступ от области графика (в точках)
)

ax.set_xlabel('Значение X', fontsize=13, color='black', labelpad=10, loc='center')
ax.set_ylabel('Значение Y', fontsize=13, color='black', labelpad=10, loc='center')

# ============================================================
# 5. ГРАНИЦЫ ОСЕЙ И МАСШТАБ
# ============================================================
ax.set_xlim(0, 10)                  # Диапазон оси X (left, right)
ax.set_ylim(-1.5, 1.5)              # Диапазон оси Y (bottom, top)
ax.set_xscale('linear')             # 'linear', 'log', 'symlog', 'logit'
ax.set_yscale('linear')
ax.set_aspect('auto')               # 'auto', 'equal', число

# ============================================================
# 6. НАСТРОЙКА ДЕЛЕНИЙ (ТИКОВ)
# ============================================================
ax.xaxis.set_major_locator(MultipleLocator(2))     # Шаг основных делений по X
ax.yaxis.set_major_locator(MultipleLocator(0.5))   # Шаг основных делений по Y
ax.xaxis.set_minor_locator(AutoMinorLocator(2))    # 2 мелких между основными
ax.yaxis.set_minor_locator(AutoMinorLocator(2))
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, pos: f'{v:.0f}'))

ax.tick_params(
    axis='both',                    # 'x', 'y', 'both'
    which='major',                  # 'major', 'minor', 'both'
    direction='out',                # 'in', 'out', 'inout'
    length=6,                       # Длина деления (в точках)
    width=1.2,                      # Толщина деления
    color='black',                  # Цвет деления
    pad=6,                          # Отступ подписи от деления
    labelsize=11,                   # Размер шрифта подписи
    labelcolor='black',             # Цвет подписи
    labelrotation=0,                # Поворот подписей (в градусах)
)

# ============================================================
# 7. СЕТКА
# ============================================================
ax.grid(
    visible=True,                   # Включить/выключить сетку
    which='major',                  # 'major', 'minor', 'both'
    axis='both',                    # 'x', 'y', 'both'
    color='gray',                   # Цвет линий сетки
    linestyle='--',                 # '-', '--', '-.', ':'
    linewidth=0.8,                  # Толщина линий
    alpha=0.5,                      # Прозрачность
)
ax.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.3)
ax.set_axisbelow(True)              # Сетка под графиком

# ============================================================
# 8. ЛЕГЕНДА
# ============================================================
ax.legend(
    loc='upper right',              # 'best', 'upper left', 'lower right', ...
    fontsize=11,                    # Размер шрифта
    title='Функции',                # Заголовок легенды
    title_fontsize=12,              # Размер шрифта заголовка
    frameon=True,                   # Рисовать ли рамку
    framealpha=0.9,                 # Прозрачность рамки
    facecolor='white',              # Цвет фона легенды
    edgecolor='gray',               # Цвет рамки
    ncol=1,                         # Количество колонок
    labelspacing=0.5,               # Расстояние между записями
    handlelength=2.0,               # Длина образца линии
    handletextpad=0.8,              # Отступ между образцом и текстом
    borderpad=0.6,                  # Внутренние отступы рамки
)

# ============================================================
# 9. ЛИНИИ, ТЕКСТ И АННОТАЦИИ
# ============================================================
ax.axhline(y=0, color='black', linewidth=0.8, linestyle='-', alpha=0.6)
ax.axvline(x=5, color='green', linestyle=':', linewidth=1, alpha=0.5)
ax.axhspan(ymin=-1.5, ymax=-1.0, color='lightblue', alpha=0.3)

ax.text(5.2, 0.1, 'Точка', fontsize=10, color='red', ha='left', va='bottom')

ax.annotate(
    'Максимум',                     # Текст
    xy=(np.pi/2, 1),                # Куда указывает стрелка
    xytext=(4, 1.3),                # Где разместить текст
    fontsize=11,
    color='darkgreen',
    arrowprops=dict(arrowstyle='->', color='darkgreen', linewidth=1.5),
    bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8),
)

# ============================================================
# 10. ОФОРМЛЕНИЕ ОБЛАСТИ ГРАФИКА (SPINES)
# ============================================================
for spine_name in ['top', 'right']:
    ax.spines[spine_name].set_visible(False)
ax.spines['left'].set_color('black')
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_color('black')
ax.spines['bottom'].set_linewidth(1.2)

# ============================================================
# 11. ФОН И ЦВЕТА
# ============================================================
ax.set_facecolor('whitesmoke')      # Цвет фона области графика
fig.patch.set_facecolor('white')    # Цвет фона всей фигуры

# ============================================================
# 12. СОХРАНЕНИЕ И ОТОБРАЖЕНИЕ
# ============================================================
# plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
plt.show()


