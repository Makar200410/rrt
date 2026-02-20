<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Кислород | Химия ЕГЭ</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Merriweather:wght@400;700&display=swap"
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

        .color-blue {
            background-color: #e3f2fd;
            border-left: 4px solid #2196f3;
            color: #0d47a1;
            padding: 10px;
            border-radius: 4px;
            margin: 10px 0;
        }

        .color-yellow {
            background-color: #fff8e1;
            border-left: 4px solid #ffc107;
            color: #f57f17;
            padding: 10px;
            border-radius: 4px;
            margin: 10px 0;
        }

        .color-gray {
            background-color: #f5f5f5;
            border-left: 4px solid #9e9e9e;
            color: #424242;
            padding: 10px;
            border-radius: 4px;
            margin: 10px 0;
        }

        .color-red {
            background-color: #fbe9e7;
            border-left: 4px solid #e64a19;
            color: #bf360c;
            padding: 10px;
            border-radius: 4px;
            margin: 10px 0;
        }

        .color-green {
            background-color: #e8f5e9;
            border-left: 4px solid #4caf50;
            color: #1b5e20;
            padding: 10px;
            border-radius: 4px;
            margin: 10px 0;
        }
        
        /* Interactive Cards */
        .interactive-cards {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            margin-top: 15px;
            margin-bottom: 25px;
        }
        .card {
            flex: 1;
            min-width: 250px;
            background: white;
            border: 1px solid #E8ECF0;
            border-radius: 12px;
            padding: 15px;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 2px 8px rgba(0,0,0,0.02);
            position: relative;
        }
        .card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.08);
            border-color: #F5A623;
        }
        .card-header {
            font-weight: 700;
            color: #1a2332;
            margin-bottom: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .card-body {
            font-size: 0.9em;
            color: #5A6A7B;
            display: none;
            padding-top: 10px;
            border-top: 1px dashed #E8ECF0;
        }
        .card.active .card-body {
            display: block;
            animation: fadeIn 0.3s ease-in-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-5px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .mnemonic-box {
            background: linear-gradient(135deg, #e3f2fd, #bbdefb);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            position: relative;
            box-shadow: 0 4px 15px rgba(33, 150, 243, 0.2);
            overflow: hidden;
        }
        .mnemonic-box::before {
            content: '☁️';
            position: absolute;
            top: -10px;
            right: -10px;
            font-size: 6rem;
            opacity: 0.15;
            font-weight: 800;
        }
        .mnemonic-title {
            font-weight: 800;
            color: #0d47a1;
            margin-bottom: 10px;
            font-size: 1.1rem;
        }
        
        .quiz-container {
            background: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 2rem;
            margin-top: 2rem;
            box-shadow: 0 8px 30px rgba(0,0,0,0.05);
        }
        .quiz-title {
            font-size: 1.4rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            color: #2c3e50;
            border-bottom: 2px solid #F5A623;
            display: inline-block;
            padding-bottom: 0.3rem;
        }
        .quiz-question {
            margin-bottom: 1.5rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px dashed #eee;
        }
        .quiz-question:last-child {
            border-bottom: none;
        }
        .quiz-q-text {
            font-weight: 600;
            margin-bottom: 1rem;
            font-size: 1.05rem;
        }
        .quiz-options {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }
        .quiz-option {
            padding: 0.8rem 1rem;
            background: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
        }
        .quiz-option:hover {
            background: #e2e6ea;
            border-color: #dae0e5;
        }
        .quiz-option input[type="radio"] {
            margin-right: 10px;
            accent-color: #F5A623;
        }
        .quiz-btn {
            background: linear-gradient(135deg, #F5A623, #d47a10);
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 1rem;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 1rem;
            transition: opacity 0.2s;
        }
        .quiz-btn:hover {
            opacity: 0.9;
        }
        .quiz-feedback {
            margin-top: 1rem;
            font-weight: 600;
            border-radius: 6px;
            padding: 10px;
            display: none;
        }
        .feedback-correct {
            background: #e8f5e9;
            color: #2e7d32;
            border: 1px solid #c8e6c9;
        }
        .feedback-incorrect {
            background: #ffebee;
            color: #c62828;
            border: 1px solid #ffcdd2;
        }

        /* Header Layout: Centered & Inline */
        header.site-header {
            display: flex;
            justify-content: center;
            padding: 0.8rem 4%;
            background: rgba(255, 255, 255, 0.98);
            border-bottom: 1px solid #E8ECF0;
            position: relative;
            z-index: 1000;
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
            height: 70px;
        }

        .header-content {
            display: flex;
            align-items: center;
            gap: 2rem;
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
            transition: all 0.2s ease;
        }

        .nav-link svg {
            width: 18px;
            height: 18px;
            stroke: currentColor;
            stroke-width: 2;
            fill: none;
        }

        .nav-link:hover {
            color: #1a2332;
            background: #F0F2F5;
        }

        .nav-link.active {
            background: #FFF4E0;
            color: #d47a10;
            font-weight: 600;
        }

        @media (max-width: 1000px) {
            .nav-link span { display: none; }
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
                <li><a href="#structure" class="active">1. Строение & Аллотропия</a></li>
                <li><a href="#production">2. Получение</a></li>
                <li><a href="#chemical-prop">3. Химические свойства</a></li>
                <li><a href="#complex-compounds">4. Реакции со сложными веществами</a></li>
                <li><a href="#quiz">5. Интерактивный тест</a></li>
            </ul>
        </aside>

        <main>
            <div class="breadcrumbs">
                <a href="../../../index.html">Главная</a> <span>/</span> <a href="../../../first_chap/theory.html">Неорганическая химия</a>
                <span>/</span> <a href="../../../first_chap/theory.html">Неметаллы</a> <span>/</span> Кислород
            </div>

            <h1>Кислород (Элемент VIA-группы)</h1>
            <p class="subtitle">Самый распространенный элемент на Земле, дыхание планеты и мощнейший окислитель (после Фтора)</p>

            <div class="info-box">
                <p><strong>Самое важное для ЕГЭ:</strong> Кислород — это <strong>сильнейший окислитель</strong>. Он вступает в реакцию почти со всей Периодической таблицей, заставляя вещества <em>гореть</em>. Единственное, что кислород окислить НЕ МОЖЕТ — это <strong>фтор</strong>, так как фтор еще "злее". Важно знать особенности горения щелочных металлов, аммиака (с катализатором и без) и сложных сульфидов.</p>
            </div>

            <!-- 1. СТРОЕНИЕ -->
            <h2 id="structure">1. Строение атома и аллотропные модификации</h2>
            <p>Кислород — первый представитель халькогенов (VIA группа, 2 период). Электронная конфигурация: <strong>1s<sup>2</sup>2s<sup>2</sup>2p<sup>4</sup></strong>. На внешнем слое 6 электронов, до заветного октета не хватает ровно двух.</p>

            <p>Типичные степени окисления:</p>
            <ul>
                <li><strong>-2</strong> — в подавляющем большинстве оксидов (H<sub>2</sub>O, CO<sub>2</sub>)</li>
                <li><strong>-1</strong> — в пероксидах (Na<sub>2</sub>O<sub>2</sub>, H<sub>2</sub>O<sub>2</sub>)</li>
                <li><strong>0</strong> — в простых веществах (O<sub>2</sub>, O<sub>3</sub>)</li>
                <li><strong>+1, +2</strong> — <strong>ТОЛЬКО ВО ФТОРИДАХ</strong> (O<sub>2</sub>F<sub>2</sub>, OF<sub>2</sub>)</li>
            </ul>

            <h3>Аллотропия (Химические воплощения)</h3>
            <p>У кислорода есть две аллотропные модификации, которые кардинально отличаются друг от друга:</p>

            <div class="interactive-cards">
                <div class="card" onclick="this.classList.toggle('active')" style="border-left: 4px solid #4fc3f7;">
                    <div class="card-header">
                        Кислород (O<sub>2</sub>) — Жизнь
                        <span style="font-size: 1.2rem; cursor: pointer;">▼</span>
                    </div>
                    <div class="card-body">
                        Газ без цвета, вкуса и запаха. Чуть тяжелее воздуха, плохо растворим в воде (но рыбам хватает!). В жидком состоянии имеет красивый светло-голубой цвет. Массовая доля в земной коре — около 47% (он входит в состав почти всех минералов: песка, глины, гранита). В воздухе его ~21% по объему.
                    </div>
                </div>
                <div class="card" onclick="this.classList.toggle('active')" style="border-left: 4px solid #1a237e;">
                    <div class="card-header">
                        Озон (O<sub>3</sub>) — Защита
                        <span style="font-size: 1.2rem; cursor: pointer;">▼</span>
                    </div>
                    <div class="card-body">
                        Газ голубого цвета со <strong>специфическим "запахом свежести"</strong> (как после грозы). Озон — гораздо более агрессивный окислитель, чем кислород (легко окисляет серебро). В высоких слоях атмосферы он образует "озоновый слой", защищающий нас от ультрафиолета. Ядовит в высоких концентрациях.
                    </div>
                </div>
            </div>

            <!-- 2. ПОЛУЧЕНИЕ -->
            <h2 id="production">2. Получение кислорода</h2>

            <h3>В промышленности</h3>
            <p>В промышленности нет смысла проводить сложные химические реакции. Воздух — это готовый коктейль газов. Воздух сжижают (превращают в жидкость при сверхнизких температурах), а затем проводят <strong>фракционную перегонку</strong> жидкого воздуха (так как у кислорода и азота разные температуры кипения).</p>

            <h3>В лаборатории</h3>
            <p>Лабораторные способы основаны на <strong>термическом разложении</strong> или каталитическом разложении богатых кислородом веществ. Эти реакции — хит первых заданий и задания №29!</p>
            
            <div style="background: rgba(255,255,255,0.8); border: 1px solid #e0e0e0; border-radius: 8px; padding: 15px; margin-bottom: 20px;">
                <p>1. Разложение Перманганата калия (марганцовки):</p>
                <p class="reaction">2KMnO<sub>4</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> K<sub>2</sub>MnO<sub>4</sub> + MnO<sub>2</sub> + O<sub>2</sub>↑</p>
                
                <hr style="border: none; border-top: 1px dashed #ccc; margin: 15px 0;">

                <p>2. Разложение Бертолетовой соли (с катализатором MnO<sub>2</sub>):</p>
                <p class="reaction">2KClO<sub>3</sub> <span class="reaction-arrow"><span class="ra-condition">MnO<sub>2</sub>, t°</span><span class="ra-symbol">→</span></span> 2KCl + 3O<sub>2</sub>↑</p>
                
                <hr style="border: none; border-top: 1px dashed #ccc; margin: 15px 0;">

                <p>3. Каталитическое разложение перекиси водорода (аптечный метод):</p>
                <p class="reaction">2H<sub>2</sub>O<sub>2</sub> <span class="reaction-arrow"><span class="ra-condition">MnO<sub>2</sub></span><span class="ra-symbol">→</span></span> 2H<sub>2</sub>O + O<sub>2</sub>↑</p>

                <hr style="border: none; border-top: 1px dashed #ccc; margin: 15px 0;">
                
                <p>4. Разложение оксидов тяжелых металлов (опыт Пристли) и нитратов:</p>
                <p class="reaction">2HgO <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> 2Hg + O<sub>2</sub>↑</p>
                <p class="reaction">2KNO<sub>3</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> 2KNO<sub>2</sub> + O<sub>2</sub>↑</p>
            </div>

            <!-- 3. ХИМИЧЕСКИЕ СВОЙСТВА -->
            <h2 id="chemical-prop">3. Химические свойства (Реакции с простыми веществами)</h2>
            <p>Кислород проявляет свойства окислителя с подавляющим большинством элементов, заставляя их гореть с выделением энергии.</p>
            
            <h3>3.1. Взаимодействие с неметаллами</h3>
            <p>Кислород окисляет почти все неметаллы (<strong>КРОМЕ ГАЛОГЕНОВ!</strong> С хлором, бромом и йодом реакций напрямую нет!).</p>

            <div class="interactive-cards">
                <div class="card" onclick="this.classList.toggle('active')">
                    <div class="card-header">С Фтором (Особый случай) <span>▼</span></div>
                    <div class="card-body">
                        Единственный элемент, которому кислород проигрывает. Фтор окисляет кислород, образуя фторид кислорода (со фтором кислород проявляет с.о. +2):<br>
                        <code>O<sub>2</sub> + 2F<sub>2</sub> → 2OF<sub>2</sub></code>
                    </div>
                </div>
                <div class="card" onclick="this.classList.toggle('active')">
                    <div class="card-header">С Углеродом (и Алмазом!) <span>▼</span></div>
                    <div class="card-body">
                        При избытке кислорода сгорает до CO<sub>2</sub>, при недостатке образуется угарный газ СО. Даже сверхтвердый алмаз сгорает в чистом кислороде без остатка!<br>
                        <code>C + O<sub>2</sub> → CO<sub>2</sub></code><br>
                        <code>2C + O<sub>2</sub><sub>(нед)</sub> → 2CO</code>
                    </div>
                </div>
            </div>

            <p><strong>С серой и кремнием (образуются устойчивые оксиды):</strong></p>
            <p class="reaction">S + O<sub>2</sub> → SO<sub>2</sub> (Образуется именно сернистый газ, SO<sub>3</sub> получить без катализатора нельзя!)</p>
            <p class="reaction">Si + O<sub>2</sub> → SiO<sub>2</sub></p>

            <p><strong>С азотом (Очень тугая реакция):</strong></p>
            <p class="reaction">N<sub>2</sub> + O<sub>2</sub> <span class="reaction-arrow"><span class="ra-condition">t=2000°C или Молния</span><span class="ra-symbol">⇄</span></span> 2NO</p>
            <p><em>(Реакция эндотермическая! Требует температуры электрической дуги, поэтому в воздухе азот и кислород годами существуют в мире и согласии.)</em></p>

            <p><strong>С фосфором:</strong></p>
            <p class="reaction">4P + 5O<sub>2(изб)</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> 2P<sub>2</sub>O<sub>5</sub></p>
            <p class="reaction">4P + 3O<sub>2(нед)</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> 2P<sub>2</sub>O<sub>3</sub></p>


            <h3>3.2. Взаимодействие с металлами</h3>
            <p>Кислород окисляет все металлы, кроме самых благородных (Золото <strong>Au</strong> и Платина <strong>Pt</strong> не горят и не окисляются).</p>

            <div class="mnemonic-box">
                <div class="mnemonic-title">ПРАВИЛО ГОРЕНИЯ ЩЕЛОЧНЫХ МЕТАЛЛОВ</div>
                <p>Классические (ожидаемые) оксиды образуются при горении <strong>только у Лития и Щёлочноземельных металлов (Ca, Ba, Sr)!</strong></p>
                <ul style="font-family: monospace; font-size: 1.1em; background: rgba(255,255,255,0.7); padding: 10px; border-radius: 6px; list-style-type: none;">
                    <li>4Li + O<sub>2</sub> → 2Li<sub>2</sub>O (Оксид)</li>
                    <li>2Ca + O<sub>2</sub> → 2CaO (Оксид)</li>
                    <li><span style="color: #c62828;">2Na + O<sub>2</sub> → Na<sub>2</sub>O<sub>2</sub> (Пероксид!)</span></li>
                    <li><span style="color: #c62828;">K + O<sub>2</sub> → KO<sub>2</sub> (Надпероксид!)</span></li>
                </ul>
            </div>

            <p>Горение переходных металлов (стандартное окисление):</p>
            <p class="reaction">2Zn + O<sub>2</sub> → 2ZnO</p>
            <p>Железо, если горит на воздухе, образует смешанный оксид (железную окалину), состоящую из FeO и Fe<sub>2</sub>O<sub>3</sub>:</p>
            <p class="reaction">3Fe + 2O<sub>2</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> Fe<sub>3</sub>O<sub>4</sub> (FeO · Fe<sub>2</sub>O<sub>3</sub>)</p>

            <!-- 4. СЛОЖНЫЕ ВЕЩЕСТВА -->
            <h2 id="complex-compounds">4. Реакции со сложными веществами (Горение)</h2>
            
            <h3>4.1 Обжиг "Пиритов" и сульфидов</h3>
            <p>Сульфиды металлов и неметаллов отлично горят в кислороде. В результате образуются <strong>два оксида</strong>: оксид металла (чаще всего до высшей устойчивой с.о.) и оксид серы(IV):</p>
            <p class="reaction">4FeS + 7O<sub>2</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> 2Fe<sub>2</sub>O<sub>3</sub> + 4SO<sub>2</sub>↑</p>
            <p class="reaction">CS<sub>2</sub> + 3O<sub>2</sub> <span class="reaction-arrow"><span class="ra-condition">t°</span><span class="ra-symbol">→</span></span> CO<sub>2</sub> + 2SO<sub>2</sub>↑ (Горение сероуглерода)</p>

            <h3>4.2 Окисление летучих водородных соединений (Аммиак и сероводород)</h3>
            <p class="reaction">2H<sub>2</sub>S + 3O<sub>2</sub> → 2H<sub>2</sub>O + 2SO<sub>2</sub> (При избытке кислорода)</p>
            <p class="reaction">2H<sub>2</sub>S + O<sub>2</sub> → 2H<sub>2</sub>O + 2S↓ (При недостатке кислорода образуется осадок серы!)</p>

            <div class="interactive-cards">
                <div class="card" onclick="this.classList.toggle('active')" style="border-left: 4px solid #f57f17;">
                    <div class="card-header">
                        Горение Аммиака (БЕЗ катализатора) <span>▼</span>
                    </div>
                    <div class="card-body">
                        Аммиак горит желтоватым пламенем, окисляясь до свободного (нейтрального) <strong>азота</strong>!<br>
                        <code style="display:block; margin-top:5px; font-weight:bold;">4NH<sub>3</sub> + 3O<sub>2</sub> → 2N<sub>2</sub> + 6H<sub>2</sub>O</code>
                    </div>
                </div>
                <div class="card" onclick="this.classList.toggle('active')" style="border-left: 4px solid #4caf50;">
                    <div class="card-header">
                        Окисление Аммиака (С КАТАЛИЗАТОРОМ) <span>▼</span>
                    </div>
                    <div class="card-body">
                        На платиновой сетке (Pt) аммиак окисляется гораздо глубже, образуя <strong>оксид азота (II)</strong>. Это важнейшая стадия получения азотной кислоты.<br>
                        <code style="display:block; margin-top:5px; font-weight:bold;">4NH<sub>3</sub> + 5O<sub>2</sub> → 4NO + 6H<sub>2</sub>O</code>
                    </div>
                </div>
            </div>

            <h3>4.3 "Дожигание" промежуточных оксидов и солей</h3>
            <p>Кислород с радостью доокисляет вещества, в которых элемент находится не в высшей степени окисления:</p>
            <p class="reaction">2NO + O<sub>2</sub> → 2NO<sub>2</sub> ("бурый газ")</p>
            <p class="reaction">2CO + O<sub>2</sub> → 2CO<sub>2</sub></p>
            <p class="reaction">4Fe(OH)<sub>2</sub> + O<sub>2</sub> + 2H<sub>2</sub>O → 4Fe(OH)<sub>3</sub> (Серо-зеленый осадок буреет на воздухе!)</p>
            
            <h3>4.4 Горение органики</h3>
            <p>Любая органика горит до углекислого газа и воды (если нет галогенов или серы):</p>
            <p class="reaction">CH<sub>4</sub> + 2O<sub>2</sub> → CO<sub>2</sub> + 2H<sub>2</sub>O</p>

            <!-- 5. ТЕСТ -->
            <h2 id="quiz">5. Интерактивный мини-тест</h2>
            <p>Проверим, как хорошо вы усвоили уловки, связанные с кислородом!</p>

            <div class="quiz-container">
                <div class="quiz-title">Экспресс-проверка: Кислород</div>
                
                <div class="quiz-question" id="q1">
                    <div class="quiz-q-text">1. Какой продукт преимущественно образуется при сгорании натрия (Na) на воздухе или в кислороде?</div>
                    <div class="quiz-options">
                        <label class="quiz-option"><input type="radio" name="q1" value="wrong"> Оксид натрия (Na₂O)</label>
                        <label class="quiz-option"><input type="radio" name="q1" value="correct"> Пероксид натрия (Na₂O₂)</label>
                        <label class="quiz-option"><input type="radio" name="q1" value="wrong"> Надпероксид натрия (NaO₂)</label>
                        <label class="quiz-option"><input type="radio" name="q1" value="wrong"> Гидроксид натрия (NaOH)</label>
                    </div>
                    <button class="quiz-btn" onclick="checkAnswer('q1')">Проверить</button>
                    <div class="quiz-feedback" id="feedback-q1"></div>
                </div>

                <div class="quiz-question" id="q2">
                    <div class="quiz-q-text">2. Что получится, если реагирует аммиак с кислородом в присутствии платинового катализатора?</div>
                    <div class="quiz-options">
                        <label class="quiz-option"><input type="radio" name="q2" value="wrong"> N₂ + H₂O</label>
                        <label class="quiz-option"><input type="radio" name="q2" value="wrong"> NO₂ + H₂O</label>
                        <label class="quiz-option"><input type="radio" name="q2" value="correct"> NO + H₂O</label>
                        <label class="quiz-option"><input type="radio" name="q2" value="wrong"> HNO₃ + H₂O</label>
                    </div>
                    <button class="quiz-btn" onclick="checkAnswer('q2')">Проверить</button>
                    <div class="quiz-feedback" id="feedback-q2"></div>
                </div>

                <div class="quiz-question" id="q3">
                    <div class="quiz-q-text">3. С каким из следующих галогенов кислород вступает в прямую химическую реакцию?</div>
                    <div class="quiz-options">
                        <label class="quiz-option"><input type="radio" name="q3" value="wrong"> Только с хлором</label>
                        <label class="quiz-option"><input type="radio" name="q3" value="wrong"> Ни с одним галогеном напрямую не реагирует</label>
                        <label class="quiz-option"><input type="radio" name="q3" value="correct"> Только с фтором</label>
                        <label class="quiz-option"><input type="radio" name="q3" value="wrong"> Со всеми галогенами (Cl₂, Br₂, I₂, F₂)</label>
                    </div>
                    <button class="quiz-btn" onclick="checkAnswer('q3')">Проверить</button>
                    <div class="quiz-feedback" id="feedback-q3"></div>
                </div>
                
                <div class="quiz-question" id="q4" style="border-bottom: none;">
                    <div class="quiz-q-text">4. Какое вещество НЕЛЬЗЯ получить термическим разложением для сбора кислорода в лаборатории (какое из реакций не выделяет кислород)?</div>
                    <div class="quiz-options">
                        <label class="quiz-option"><input type="radio" name="q4" value="correct"> Карбонат кальция (CaCO₃)</label>
                        <label class="quiz-option"><input type="radio" name="q4" value="wrong"> Перманганат калия (KMnO₄)</label>
                        <label class="quiz-option"><input type="radio" name="q4" value="wrong"> Бертолетова соль (KClO₃)</label>
                        <label class="quiz-option"><input type="radio" name="q4" value="wrong"> Пероксид водорода (H₂O₂)</label>
                    </div>
                    <button class="quiz-btn" onclick="checkAnswer('q4')">Проверить</button>
                    <div class="quiz-feedback" id="feedback-q4"></div>
                </div>
            </div>

            <script>
                function checkAnswer(questionId) {
                    const radios = document.getElementsByName(questionId);
                    const feedback = document.getElementById('feedback-' + questionId);
                    let selectedValue = null;

                    for (const radio of radios) {
                        if (radio.checked) {
                            selectedValue = radio.value;
                            break;
                        }
                    }

                    feedback.style.display = 'block';
                    if (selectedValue === 'correct') {
                        feedback.textContent = '✅ Верно! Отличная работа.';
                        feedback.className = 'quiz-feedback feedback-correct';
                    } else if (selectedValue === 'wrong') {
                        feedback.textContent = '❌ Неверно. Внимательно перечитай теорию выше!';
                        feedback.className = 'quiz-feedback feedback-incorrect';
                    } else {
                        feedback.textContent = '⚠️ Пожалуйста, выбери вариант ответа.';
                        feedback.className = 'quiz-feedback feedback-incorrect';
                        feedback.style.background = '#fff3cd';
                        feedback.style.color = '#856404';
                        feedback.style.borderColor = '#ffeeba';
                    }
                }
            </script>

            <!-- НАВИГАЦИЯ -->
            <div style="margin-top: 3rem; display: flex; justify-content: space-between;">
                <a href="../halogens/halogens.html" class="prev-chapter"
                    style="padding: 10px 20px; background-color: white; border: 1px solid var(--border-color); color: var(--text-primary); text-decoration: none; border-radius: 8px; font-weight: 500; font-size: 0.9rem;">
                    ← Галогены
                </a>
                <a href="../../../tests/periodic_law_test.html" class="next-chapter"
                    style="padding: 10px 20px; background-color: var(--text-accent); color: white; text-decoration: none; border-radius: 8px; font-weight: 500; font-size: 0.9rem;">
                    Азот и Фосфор →
                </a>
            </div>

        </main>
    </div>

    <footer>
            <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 0.3rem 1rem; margin-bottom: 0.5rem; margin-top: 2rem;">
                <a href="../../../index.html" style="color: var(--text-secondary); text-decoration: none;">Главная</a><span style="color: #ddd;">·</span>
                <a href="../../../first_chap/theory.html" style="color: var(--text-secondary); text-decoration: none;">Теория</a><span style="color: #ddd;">·</span>
                <a href="../../../tests/periodic_law_test.html" style="color: var(--text-secondary); text-decoration: none;">Задания</a><span style="color: #ddd;">·</span>
                <a href="../../../variants.html" style="color: var(--text-secondary); text-decoration: none;">Варианты</a><span style="color: #ddd;">·</span>
                <a href="../../../courses.html" style="color: var(--text-secondary); text-decoration: none;">Курсы</a><span style="color: #ddd;">·</span>
                <a href="../../../dashboard.html" style="color: var(--text-secondary); text-decoration: none;">Панель</a>
            </div>
            <p style="text-align: center; color: #666;">© 2025 ХимПодготовка — подготовка к ЕГЭ по химии</p>
    </footer>

</body>

</html>
