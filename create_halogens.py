import os

html_content = """<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Галогены | Химия ЕГЭ</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Merriweather:wght@400;700&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="../../../style.css">
    <style>
        .reaction-arrow {
            display: inline-flex;
            flex-direction: column;
            align-items: center;
            vertical-align: middle;
            margin: 0 4px;
            position: relative;
            top: -5px;
        }

        .ra-condition {
            font-size: 0.75em;
            line-height: 1;
            margin-bottom: 0px;
            color: #d32f2f;
            font-weight: 500;
        }

        .ra-symbol {
            line-height: 1;
            font-size: 1.2em;
            font-family: 'Times New Roman', serif;
            margin-top: -2px;
        }

        .color-box {
            padding: 10px;
            border-radius: 4px;
            margin: 5px 0;
            font-weight: 500;
        }

        .color-blue {
            background-color: #e3f2fd;
            border-left: 4px solid #2196f3;
            color: #0d47a1;
        }

        .color-yellow {
            background-color: #fff8e1;
            border-left: 4px solid #ffc107;
            color: #f57f17;
        }

        .color-gray {
            background-color: #f5f5f5;
            border-left: 4px solid #9e9e9e;
            color: #424242;
        }

        .color-red {
            background-color: #fbe9e7;
            border-left: 4px solid #e64a19;
            color: #bf360c;
        }

        .color-green {
            background-color: #e8f5e9;
            border-left: 4px solid #4caf50;
            color: #1b5e20;
        }

        /* Header Layout: Centered & Inline */
        header.site-header {
            display: flex;
            justify-content: center;
            /* Centers the inner wrapper */
            padding: 0.8rem 4%;
            background: rgba(255, 255, 255, 0.98);
            border-bottom: 1px solid #E8ECF0;
            position: relative;
            z-index: 1000;
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
            height: 70px;
        }

        /* Wrapper to keep Logo and Nav together and centered */
        .header-content {
            display: flex;
            align-items: center;
            gap: 2rem;
            /* Spacing between Logo and Nav */
        }

        header.site-header .logo {
            font-size: 1.3rem;
            font-weight: 800;
            color: #1a2332;
            text-decoration: none;
            white-space: nowrap;
        }

        header.site-header .logo span {
            color: #F5A623;
        }

        /* Nav Container */
        .site-nav-container {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .nav-link {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            border-radius: 12px;
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            color: #5A6A7B;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid transparent;
        }

        .nav-link svg {
            width: 18px;
            height: 18px;
            stroke: currentColor;
            stroke-width: 2;
            fill: none;
            transition: transform 0.2s ease;
        }

        /* Hover State */
        .nav-link:hover {
            color: #1a2332;
            background: #F0F2F5;
            transform: translateY(-1px);
        }

        .nav-link:hover svg {
            transform: scale(1.1);
            stroke: #E8941A;
        }

        /* Active State */
        .nav-link.active {
            background: #FFF4E0;
            color: #d47a10;
            font-weight: 600;
            border-color: rgba(245, 166, 35, 0.2);
        }

        .nav-link.active svg {
            stroke: #d47a10;
        }

        @media (max-width: 1000px) {
            .nav-link span {
                display: none;
            }
        }
    </style>
</head>

<body class="with-sidebar">

    <header class="site-header">
        <div class="header-content">
            <a href="../../../index.html" class="logo">
                Хим<span>Подготовка</span>
            </a>

            <nav class="site-nav-container">
                <a href="../../../index.html" class="nav-link">
                    <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                        <polyline points="9 22 9 12 15 12 15 22"></polyline>
                    </svg>
                    <span>Главная</span>
                </a>
                <a href="../../../first_chap/theory.html" class="nav-link">
                    <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                    </svg>
                    <span>Теория</span>
                </a>
                <a href="../../../tests/periodic_law_test.html" class="nav-link">
                    <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
                    </svg>
                    <span>Задания</span>
                </a>
                <a href="../../../variants.html" class="nav-link">
                    <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                        <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
                        <polyline points="2 17 12 22 22 17"></polyline>
                        <polyline points="2 12 17 12"></polyline>
                    </svg>
                    <span>Варианты</span>
                </a>
                <a href="../../../courses.html" class="nav-link">
                    <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M22 10v6M2 10l10-5 10 5-10 5z"></path>
                        <path d="M6 12v5c3 3 9 3 12 0v-5"></path>
                    </svg>
                    <span>Курсы</span>
                </a>
                <a href="../../../dashboard.html" class="nav-link">
                    <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="18" y1="20" x2="18" y2="10"></line>
                        <line x1="12" y1="20" x2="12" y2="4"></line>
                        <line x1="6" y1="20" x2="6" y2="14"></line>
                    </svg>
                    <span>Панель</span>
                </a>
            </nav>
        </div>
    </header>

    <div class="container">
        <aside>
            <h3>Оглавление</h3>
            <ul>
                <li><a href="#structure" class="active">1. Строение атомов</a></li>
                <li><a href="#physical">2. Физические свойства</a></li>
                <li><a href="#production">3. Получение галогенов</a></li>
                <li><a href="#chemical-prop">4. Свойства простых веществ</a></li>
                <li><a href="#hydrogen-halides">5. Галогеноводороды</a></li>
                <li><a href="#qualitative">6. Качественные реакции</a></li>
            </ul>
        </aside>

        <main>
            <div class="breadcrumbs">
                <a href="../../../index.html">Главная</a> <span>/</span> <a href="../../../first_chap/theory.html">Неорганическая химия</a>
                <span>/</span> <a href="../../../first_chap/theory.html">Неметаллы</a> <span>/</span> Галогены
            </div>

            <h1>Галогены (Элементы VIIA-группы)</h1>
            <p class="subtitle">Типичные неметаллы (Фтор, Хлор, Бром, Иод), бешеные окислители и "рождающие соли"</p>

            <div class="info-box">
                <p><strong>Важно для ЕГЭ:</strong> Галогены — <strong>сильные окислители</strong> (особенно фтор F<sub>2</sub>, который окисляет даже кислород). В реакциях с металлами они образуют соли высших степеней окисления. Галогены <strong>не реагируют</strong> напрямую с кислородом O<sub>2</sub>, азотом N<sub>2</sub> и благородными газами. При растворении в воде и щелочах <strong>диспропорционируют</strong> (кроме фтора, который воду окисляет со взрывом).</p>
            </div>

            <!-- 1. СТРОЕНИЕ -->
            <h2 id="structure">1. Строение атомов и положение в ПСХЭ</h2>
            <p>Галогены — это элементы VIIA-группы таблицы Менделеева: <strong>фтор (F), хлор (Cl), бром (Br), иод (I), астат (At)</strong>. Астат — редчайший радиоактивный элемент, поэтому в школьном курсе он практически не встречается.</p>

            <h3>Электронная конфигурация</h3>
            <div
                style="background: #f8f9fa; padding: 15px; border-radius: 8px; text-align: center; font-size: 1.1em; border: 1px solid #e9ecef; margin: 15px 0;">
                <p style="margin: 8px 0;">Общая электронная конфигурация внешнего уровня: <strong>ns<sup>2</sup>np<sup>5</sup></strong></p>
                <p style="font-size:0.85em; color: #555;">(имеют 7 электронов на внешнем уровне, не хватает одного до завершения)</p>
            </div>
            
            <p><strong>Возможные степени окисления:</strong></p>
            <ul>
                <li><strong>Фтор (F)</strong>: У фтора <strong>навсегда</strong> и единственная отрицательная с.о. <strong>-1</strong> (ну и <strong>0</strong> в простом веществе). У него нет d-орбитали, он не может распаривать электроны и повышать с.о. Фтор — самый электроотрицательный элемент Периодической системы.</li>
                <li><strong>Хлор (Cl), Бром (Br), Иод (I)</strong>: Благодаря наличию d-орбиталей могут распаривать свои внешние электроны. Для них характерны степени окисления: <strong>-1, 0, +1, +3, +5, +7</strong> (нечетные, как и номер группы).</li>
            </ul>

            <!-- 2. ФИЗИЧЕСКИЕ СВОЙСТВА -->
            <h2 id="physical">2. Физические свойства</h2>
            <p>Простые вещества галогены существуют в виде <strong>двухатомных молекул</strong>: F<sub>2</sub>, Cl<sub>2</sub>, Br<sub>2</sub>, I<sub>2</sub>. Имеют молекулярную кристаллическую решетку.</p>

            <table class="styled-table">
                <thead>
                    <tr>
                        <th>Галоген</th>
                        <th>Агрегатное состояние (н.у.)</th>
                        <th>Цвет и особенности</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Фтор (F<sub>2</sub>)</strong></td>
                        <td>Газ</td>
                        <td>Бледно-желтый, резкий запах, ядовит.</td>
                    </tr>
                    <tr>
                        <td><strong>Хлор (Cl<sub>2</sub>)</strong></td>
                        <td>Газ</td>
                        <td>Желто-зеленый, тяжелее воздуха, резкий удушливый запах, ядовит.</td>
                    </tr>
                    <tr>
                        <td><strong>Бром (Br<sub>2</sub>)</strong></td>
                        <td>Жидкость</td>
                        <td>Тяжелая красно-бурая летучая жидкость, неприятный запах, пары токсичны.</td>
                    </tr>
                    <tr>
                        <td><strong>Иод (I<sub>2</sub>)</strong></td>
                        <td>Твердое вещество</td>
                        <td>Темно-серо-фиолетовые кристаллы с металлическим блеском.</td>
                    </tr>
                </tbody>
            </table>

            <div class="clarification-frame">
                <strong>Интересный факт (Возгонка):</strong> Твердый кристаллический иод I<sub>2</sub> при небольшом нагревании переходит в фиолетовый газ, <strong>минуя жидкое состояние</strong>. Этот удивительный процесс называется возгонкой (сублимацией)!
            </div>

            <!-- 3. ПОЛУЧЕНИЕ -->
            <h2 id="production">3. Получение галогенов</h2>

            <h3>В промышленности</h3>
            <p>Получают крайне энергозатратным, но единственно верным способом — <strong>электролизом</strong> (растворов или расплавов солей).</p>
            <p><strong>Электролиз раствора хлорида натрия (получение хлора, щелочи и водорода):</strong></p>
            <p class="reaction">2NaCl + 2H<sub>2</sub>O <span class="reaction-arrow"><span class="ra-condition">электроток</span><span class="ra-symbol">→</span></span> H<sub>2</sub>↑ (на катоде) + Cl<sub>2</sub>↑ (на аноде) + 2NaOH</p>
            <p><strong>Электролиз расплава хлорида натрия (получение хлора и металлического натрия):</strong></p>
            <p class="reaction">2NaCl<sub>(расплав)</sub> <span class="reaction-arrow"><span class="ra-condition">электроток</span><span class="ra-symbol">→</span></span> 2Na + Cl<sub>2</sub>↑</p>
            <p><em>(Фтор получают электролизом расплава солей, например, KHF<sub>2</sub>).</em></p>

            <h3>В лаборатории</h3>
            <p>В лаборатории хлор получают взаимодействием концентрированной соляной кислоты (HCl) с сильными окислителями.</p>
            <p class="reaction">MnO<sub>2</sub> + 4HCl<sub>(конц.)</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> MnCl<sub>2</sub> + Cl<sub>2</sub>↑ + 2H<sub>2</sub>O</p>
            <p class="reaction">2KMnO<sub>4</sub> + 16HCl<sub>(конц.)</sub> → 2MnCl<sub>2</sub> + 2KCl + 5Cl<sub>2</sub>↑ + 8H<sub>2</sub>O</p>
            <p class="reaction">KClO<sub>3</sub> + 6HCl<sub>(конц.)</sub> → KCl + 3Cl<sub>2</sub>↑ + 3H<sub>2</sub>O</p>
            
            <p>Также галогены можно получить <strong>вытеснением менее активных галогенов более активными</strong>:</p>
            <p class="reaction">Cl<sub>2</sub> + 2KI → 2KCl + I<sub>2</sub>↓</p>
            <p class="reaction">Cl<sub>2</sub> + 2HBr → 2HCl + Br<sub>2</sub></p>
            <p><em>(Активность галогенов убывает сверху вниз: <strong>F &gt; Cl &gt; Br &gt; I</strong>).</em></p>


            <!-- 4. ХИМИЧЕСКИЕ СВОЙСТВА -->
            <h2 id="chemical-prop">4. Химические свойства простых веществ</h2>
            <p>Химическая активность галогенов уменьшается от фтора к иоду. Все галогены проявляют мощные окислительные свойства.</p>

            <h3>1. Взаимодействие с металлами</h3>
            <p>Галогены энергично реагируют почти со всеми металлами. Чаще всего они окисляют металл до высшей (или одной из самых устойчивых высших) степени окисления.</p>
            <p class="reaction">2Fe + 3Cl<sub>2</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> 2FeCl<sub>3</sub> (окисляется до +3)</p>
            <p class="reaction">Fe + I<sub>2</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> FeI<sub>2</sub> (йод более слабый, только до +2)</p>
            <p class="reaction">Cu + Cl<sub>2</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> CuCl<sub>2</sub> (с йодом образуется только CuI)</p>

            <h3>2. Взаимодействие с неметаллами</h3>
            <p>С водородом реакции идут в зависимости от активности:</p>
            <ul>
                <li><span class="reaction">F<sub>2</sub> + H<sub>2</sub> → 2HF</span> (со взрывом, даже в темноте)</li>
                <li><span class="reaction">Cl<sub>2</sub> + H<sub>2</sub> <span class="reaction-arrow"><span class="ra-condition">hν (свет)</span><span class="ra-symbol">→</span></span> 2HCl</span> (на свету со взрывом)</li>
                <li><span class="reaction">Br<sub>2</sub> + H<sub>2</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> 2HBr</span> (при нагревании)</li>
                <li><span class="reaction">I<sub>2</sub> + H<sub>2</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">⇄</span></span> 2HI</span> (эндотермическая обратимая реакция)</li>
            </ul>

            <p>С фосфором галогены реагируют, формируя галогениды P(III) или P(V) в зависимости от избытка/недостатка:</p>
            <p class="reaction">2P + 5Cl<sub>2</sub><sub>(изб.)</sub> → 2PCl<sub>5</sub></p>
            <p class="reaction">2P + 3Cl<sub>2</sub><sub>(нед.)</sub> → 2PCl<sub>3</sub></p>

            <div class="color-red">
                <strong>Исключения для реакций с неметаллами:</strong> Все галогены (даже сильнейший фтор) напрямую <strong>НЕ реагируют</strong> с кислородом (O<sub>2</sub>), азотом (N<sub>2</sub>) и углеродом (алмазом)!
            </div>

            <h3>3. Реакции со сложными веществами (Вода и Щелочи)</h3>
            <p>Фтор вступает в реакцию окисления (вода становится восстановителем):</p>
            <p class="reaction">2F<sub>2</sub> + 2H<sub>2</sub>O → 4HF + O<sub>2</sub>↑ (горение воды во фторе)</p>
            
            <p>Сложные реакции диспропорционирования (самореакций) <strong>хлора и брома</strong> в воде:</p>
            <ul>
                <li>В холодной воде образуются 2 кислоты (с.о. +1 и -1): <br><span class="reaction">Cl<sub>2</sub> + H<sub>2</sub>O ⇄ HCl + HClO</span> (хлорноватистая кислота)</li>
                <li>В горячей воде образуются 2 кислоты (с.о. +5 и -1): <br><span class="reaction">3Cl<sub>2</sub> + 6H<sub>2</sub>O ⇄ 5HCl + HClO<sub>3</sub></span> (хлорноватая кислота)</li>
            </ul>
            
            <p>Реакции <strong>хлора и брома</strong> со щелочами (алгоритмы 1 в 1 как с водой):</p>
            <ul>
                <li>В холодном растворе щёлочи образуются 2 соли (с.о. +1 и -1): <br><span class="reaction">Cl<sub>2</sub> + 2NaOH<sub>(холод.)</sub> → NaCl + NaClO + H<sub>2</sub>O</span> (Жавелевая вода)</li>
                <li>В горячем растворе щёлочи образуются 2 соли (с.о. +5 и -1): <br><span class="reaction">3Cl<sub>2</sub> + 6NaOH<sub>(горяч.)</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> 5NaCl + NaClO<sub>3</sub> + 3H<sub>2</sub>O</span> (Бертолетова соль)</li>
            </ul>

            <!-- 5. ГАЛОГЕНОВОДОРОДЫ -->
            <h2 id="hydrogen-halides">5. Галогеноводороды (HF, HCl, HBr, HI)</h2>
            <p>Это газы (кроме фтороводорода, который является жидкостью до 19.5 °C за счёт мощных водородных связей), хорошо растворимые в воде с образованием кислот. </p>
            <p><strong>Кислотные свойства растут</strong> в ряду: HF &lt; HCl &lt; HBr &lt; HI. Таким образом, плавиковая кислота (HF) — слабая, а все остальные — <strong>очень сильные кислоты</strong>.</p>
            <p><strong>Восстановительные свойства солей</strong> также растут от фтора к иоду. Иодоводород (HI) — один из сильнейших восстановителей неорганики!</p>
            <p class="reaction">2HI + H<sub>2</sub>SO<sub>4(конц.)</sub> → I<sub>2</sub>↓ + H<sub>2</sub>S↑ + 4H<sub>2</sub>O</p>
            <p class="reaction">6HI + 2H<sub>2</sub>SO<sub>4(конц.)</sub> → 3I<sub>2</sub>↓ + S↓ + 4H<sub>2</sub>O + (SO<sub>2</sub>)</p>
            <p class="reaction">2HI + 2FeCl<sub>3</sub> → I<sub>2</sub>↓ + 2FeCl<sub>2</sub> + 2HCl</p>

            <div class="color-blue">
                <strong>Плавиковая кислота и стекло:</strong> Раствор фтороводорода — <strong>плавиковая кислота HF</strong> — обладает уникальным свойством растворять чистое стекло и песок (оксид кремния SiO<sub>2</sub>), образуя газ фторид кремния. Именно поэтому её запрещено хранить в стеклянной посуде (хранят только в пластиковых или парафиновых баночках)! <br>
                <code style="display:block; margin-top: 10px;">SiO<sub>2</sub> + 4HF → SiF<sub>4</sub>↑ + 2H<sub>2</sub>O</code>
            </div>

            <!-- 6. КАЧЕСТВЕННЫЕ РЕАКЦИИ -->
            <h2 id="qualitative">6. Качественные реакции</h2>
            <p>Качественными реакциями на присутствие галогенид-ионов (Cl<sup>-</sup>, Br<sup>-</sup>, I<sup>-</sup>) является добавление растворимых солей серебра (например, AgNO<sub>3</sub>). При этом выпадают характерные осадки галогенидов серебра (AgHal), которые <strong>не растворяются в минеральных кислотах</strong> (например, в HNO<sub>3</sub>).</p>

            <ul>
                <li><strong>Хлорид-ион (Cl<sup>-</sup>):</strong> Выпадение <strong>белого творожистого</strong> осадка AgCl. <br><span class="reaction">NaCl + AgNO<sub>3</sub> → AgCl↓ + NaNO<sub>3</sub></span></li>
                <li><strong>Бромид-ион (Br<sup>-</sup>):</strong> Выпадение <strong>светло-желтого (желтоватого)</strong> осадка AgBr. <br><span class="reaction">NaBr + AgNO<sub>3</sub> → AgBr↓ + NaNO<sub>3</sub></span></li>
                <li><strong>Йодид-ион (I<sup>-</sup>):</strong> Выпадение <strong>насыщенно желтого</strong> осадка AgI. <br><span class="reaction">NaI + AgNO<sub>3</sub> → AgI↓ + NaNO<sub>3</sub></span></li>
            </ul>
            <div class="color-gray">
                <strong>Важно:</strong> Фторид серебра (AgF) — <strong>хорошо растворимая</strong> соль. Осадка при добавлении нитрата серебра к фторидам не будет!
            </div>

            <!-- БЛОК ТЕСТА -->
            <div
                style="background: linear-gradient(135deg, #1a2332 0%, #243447 100%); border-radius: 12px; padding: 1.5rem 2rem; display: flex; align-items: center; justify-content: space-between; gap: 1.5rem; flex-wrap: wrap; margin-top: 2.5rem;">
                <div style="flex: 1; min-width: 200px;">
                    <div style="font-size: 1.05rem; font-weight: 700; color: #fff; margin-bottom: 0.3rem;">🎯 Пройди
                        тест по теме</div>
                    <div style="font-size: 0.82rem; color: rgba(255,255,255,0.55); line-height: 1.5;">Проверь свои
                        знания. Задания формата ЕГЭ.</div>
                </div>
                <a href="../../../tests/periodic_law_test.html"
                    style="padding: 0.6rem 1.3rem; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 0.85rem; background: linear-gradient(135deg, #F5A623, #e8941a); color: #fff; white-space: nowrap;">Начать
                    тест →</a>
            </div>

            <div style="margin-top: 2rem; display: flex; justify-content: space-between;">
                <a href="../hydrogen/hydrogen.html" class="prev-chapter"
                    style="padding: 10px 20px; background-color: white; border: 1px solid var(--border-color); color: var(--text-primary); text-decoration: none; border-radius: 8px; font-weight: 500; font-size: 0.9rem;">
                    ← Водород
                </a>
                <a href="../../../tests/periodic_law_test.html" class="next-chapter"
                    style="padding: 10px 20px; background-color: var(--text-accent); color: white; text-decoration: none; border-radius: 8px; font-weight: 500; font-size: 0.9rem;">
                    Кислород →
                </a>
            </div>

        </main>
    </div>

    <footer>
            <div
                style="display: flex; justify-content: center; flex-wrap: wrap; gap: 0.3rem 1rem; margin-bottom: 0.5rem; margin-top: 2rem;">
                <a href="../../../index.html"
                    style="color: var(--text-secondary); text-decoration: none;">Главная</a>
                <span style="color: #ddd;">·</span>
                    <a href="../../../first_chap/theory.html"
                        style="color: var(--text-secondary); text-decoration: none;">Теория</a>
                    <span style="color: #ddd;">·</span>
                    <a href="../../../tests/periodic_law_test.html"
                        style="color: var(--text-secondary); text-decoration: none;">Задания</a>
                    <span style="color: #ddd;">·</span>
                    <a href="../../../variants.html"
                        style="color: var(--text-secondary); text-decoration: none;">Варианты</a>
                    <span style="color: #ddd;">·</span>
                    <a href="../../../courses.html"
                        style="color: var(--text-secondary); text-decoration: none;">Курсы</a>
                    <span style="color: #ddd;">·</span>
                    <a href="../../../dashboard.html"
                        style="color: var(--text-secondary); text-decoration: none;">Панель</a>
                </div>
                <p style="text-align: center; color: #666;">© 2025 ХимПодготовка — подготовка к ЕГЭ по химии</p>
    </footer>

</body>

</html>
"""

with open(r'c:\Users\B-Zone\Documents\chem\inorganic\nonmetals\halogens\halogens.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Created halogens.html successfully")
