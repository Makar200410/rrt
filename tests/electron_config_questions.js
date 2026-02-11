// ===== 50 QUESTIONS: ЭЛЕКТРОННЫЕ КОНФИГУРАЦИИ (Задание 1 ЕГЭ) =====
const questions = [
    // --- Тип 1: Определение элемента по электронной конфигурации ---
    {
        text: "Какой элемент имеет электронную конфигурацию 1s²2s²2p⁶3s²3p⁶?",
        answers: ["Калий (K)", "Аргон (Ar)", "Хлор (Cl)", "Кальций (Ca)"],
        correct: 1,
        hint: "Посчитайте общее число электронов: 2+2+6+2+6 = 18. Какой элемент имеет Z=18?"
    },
    {
        text: "Электронная конфигурация 1s²2s²2p⁶3s¹ соответствует атому:",
        answers: ["Лития", "Натрия", "Калия", "Магния"],
        correct: 1,
        hint: "Общее число электронов = 11. Найдите элемент с Z=11."
    },
    {
        text: "Какому элементу соответствует конфигурация 1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁵?",
        answers: ["Селен (Se)", "Бром (Br)", "Криптон (Kr)", "Мышьяк (As)"],
        correct: 1,
        hint: "Подсчитайте все электроны: 2+2+6+2+6+10+2+5 = 35. Z=35 — это бром."
    },
    {
        text: "Атом какого элемента имеет конфигурацию [Ne]3s²3p³?",
        answers: ["Кремний (Si)", "Фосфор (P)", "Сера (S)", "Алюминий (Al)"],
        correct: 1,
        hint: "[Ne] = 10 электронов, + 2 + 3 = 15. Элемент с Z=15 — это фосфор."
    },
    {
        text: "Электронная конфигурация [Ar]3d⁵4s¹ соответствует атому:",
        answers: ["Марганца (Mn)", "Хрома (Cr)", "Ванадия (V)", "Железа (Fe)"],
        correct: 1,
        hint: "Это пример «провала» электрона. [Ar]=18, +5+1 = 24. Z=24 — хром."
    },

    // --- Тип 2: Число электронов на внешнем уровне ---
    {
        text: "Сколько электронов на внешнем энергетическом уровне у атома серы (S)?",
        answers: ["4", "6", "2", "8"],
        correct: 1,
        hint: "Сера в VI группе, главная подгруппа. Число внешних электронов = номеру группы."
    },
    {
        text: "У атомов каких двух элементов на внешнем уровне 4 электрона? \n1) Na  2) Si  3) P  4) C  5) Cl",
        answers: ["2 и 4", "1 и 3", "3 и 5", "1 и 5"],
        correct: 0,
        hint: "Четыре внешних электрона имеют элементы IV группы: кремний (Si) и углерод (C)."
    },
    {
        text: "У атомов каких двух элементов на внешнем уровне 1 электрон? \n1) Na  2) Cl  3) S  4) K  5) Al",
        answers: ["2 и 5", "1 и 4", "3 и 4", "1 и 5"],
        correct: 1,
        hint: "Один электрон на внешнем уровне — это элементы I группы: Na и K."
    },
    {
        text: "У атомов каких двух элементов на внешнем уровне 5 электронов? \n1) P  2) S  3) N  4) O  5) Fe",
        answers: ["2 и 4", "1 и 5", "1 и 3", "3 и 5"],
        correct: 2,
        hint: "Пять электронов на внешнем уровне — это элементы V группы: фосфор (P) и азот (N)."
    },
    {
        text: "У атомов каких двух элементов на внешнем уровне 2 электрона? \n1) Be  2) B  3) N  4) Mg  5) Cl",
        answers: ["1 и 4", "2 и 3", "1 и 5", "3 и 4"],
        correct: 0,
        hint: "Два электрона на внешнем уровне — элементы II группы: бериллий (Be) и магний (Mg)."
    },

    // --- Тип 3: Распределение электронов по подуровням ---
    {
        text: "Какая электронная конфигурация верна для атома железа (Fe, Z=26)?",
        answers: ["[Ar]3d⁶4s²", "[Ar]3d⁸", "[Ar]3d⁷4s¹", "[Ar]3d⁵4s²4p¹"],
        correct: 0,
        hint: "Железо: [Ar] + 6 электронов на 3d + 2 на 4s."
    },
    {
        text: "Какая электронная конфигурация правильная для атома меди (Cu, Z=29)?",
        answers: ["[Ar]3d⁹4s²", "[Ar]3d¹⁰4s¹", "[Ar]3d⁸4s²4p¹", "[Ar]3d¹⁰4s²"],
        correct: 1,
        hint: "У меди «провал» электрона: полностью заполненный 3d¹⁰ энергетически выгоднее."
    },
    {
        text: "Сколько электронов на 3d-подуровне у атома титана (Ti, Z=22)?",
        answers: ["4", "2", "3", "1"],
        correct: 1,
        hint: "Ti: [Ar]3d²4s². На 3d-подуровне 2 электрона."
    },
    {
        text: "Какая конфигурация внешнего уровня у атома хлора (Cl)?",
        answers: ["3s²3p⁴", "3s²3p⁵", "3s²3p⁶", "3s²3p³"],
        correct: 1,
        hint: "Хлор в VII группе, 3-й период. Внешний уровень: 3s²3p⁵."
    },
    {
        text: "Электронная конфигурация валентных электронов атома германия (Ge):",
        answers: ["4s²4p⁴", "4s²4p²", "4s²4p³", "4s²3d²"],
        correct: 1,
        hint: "Германий в IV группе, главная подгруппа, 4-й период: 4s²4p²."
    },

    // --- Тип 4: Электронные конфигурации ионов ---
    {
        text: "Какая электронная конфигурация у иона Na⁺?",
        answers: ["1s²2s²2p⁶3s¹", "1s²2s²2p⁶", "1s²2s²2p⁵", "1s²2s²2p⁶3s²"],
        correct: 1,
        hint: "Na⁺ теряет 1 электрон: 11 - 1 = 10 электронов, конфигурация неона."
    },
    {
        text: "Электронная конфигурация иона Cl⁻ совпадает с конфигурацией атома:",
        answers: ["Серы (S)", "Фтора (F)", "Аргона (Ar)", "Калия (K)"],
        correct: 2,
        hint: "Cl⁻ имеет 17+1=18 электронов — такая же конфигурация, как у аргона."
    },
    {
        text: "Сколько электронов в ионе Fe³⁺?",
        answers: ["29", "23", "26", "25"],
        correct: 1,
        hint: "Fe имеет 26 электронов, Fe³⁺ теряет 3: 26-3 = 23."
    },
    {
        text: "Какая электронная конфигурация у иона Fe²⁺?",
        answers: ["[Ar]3d⁶4s²", "[Ar]3d⁶", "[Ar]3d⁵4s¹", "[Ar]3d⁴4s²"],
        correct: 1,
        hint: "При образовании катионов d-элементы сначала теряют s-электроны. Fe²⁺: [Ar]3d⁶."
    },
    {
        text: "Электронная конфигурация какого иона: 1s²2s²2p⁶?",
        answers: ["Только Na⁺", "Только F⁻", "Na⁺, F⁻, Mg²⁺, O²⁻, Al³⁺", "Только Ne"],
        correct: 2,
        hint: "Конфигурация с 10 электронами свойственна многим ионам: Na⁺, F⁻, Mg²⁺, O²⁻, Al³⁺ — изоэлектронные частицы."
    },

    // --- Тип 5: Число неспаренных электронов ---
    {
        text: "Сколько неспаренных электронов в основном состоянии у атома азота (N)?",
        answers: ["1", "2", "3", "5"],
        correct: 2,
        hint: "N: 1s²2s²2p³. На 2p-подуровне 3 электрона, по правилу Хунда все неспаренные."
    },
    {
        text: "У атома какого элемента 2 неспаренных электрона? \n1) Be  2) C  3) N  4) Ne",
        answers: ["1) Be", "2) C", "3) N", "4) Ne"],
        correct: 1,
        hint: "C: 1s²2s²2p². На 2p — два неспаренных электрона (правило Хунда)."
    },
    {
        text: "Сколько неспаренных электронов у атома кислорода (O) в основном состоянии?",
        answers: ["0", "1", "2", "4"],
        correct: 2,
        hint: "O: 1s²2s²2p⁴. На 2p: ↑↓ ↑ ↑ — два неспаренных."
    },
    {
        text: "У какого атома в основном состоянии нет неспаренных электронов?",
        answers: ["Кислород (O)", "Бериллий (Be)", "Бор (B)", "Фтор (F)"],
        correct: 1,
        hint: "Be: 1s²2s². Все электроны спарены."
    },
    {
        text: "Сколько неспаренных электронов у атома хрома (Cr) в основном состоянии?",
        answers: ["4", "5", "6", "1"],
        correct: 2,
        hint: "Cr: [Ar]3d⁵4s¹. На 3d — 5 неспаренных, на 4s — 1. Итого 6."
    },

    // --- Тип 6: s-, p-, d-элементы ---
    {
        text: "Какой из элементов является d-элементом?",
        answers: ["Кальций (Ca)", "Скандий (Sc)", "Галлий (Ga)", "Германий (Ge)"],
        correct: 1,
        hint: "d-элементы — те, у которых заполняется d-подуровень. Sc: [Ar]3d¹4s²."
    },
    {
        text: "К какому семейству (s, p, d, f) относится элемент с конфигурацией [Xe]4f¹⁴5d¹6s²?",
        answers: ["s-элемент", "p-элемент", "d-элемент", "f-элемент"],
        correct: 2,
        hint: "Последний заполняемый подуровень — 5d, значит это d-элемент (лютеций)."
    },
    {
        text: "Какие из перечисленных элементов являются p-элементами? \n1) Na  2) Al  3) Fe  4) Cl  5) Cu",
        answers: ["1 и 3", "2 и 4", "3 и 5", "1 и 5"],
        correct: 1,
        hint: "Al и Cl — у них последний электрон заполняет p-подуровень."
    },
    {
        text: "Элемент с электронной конфигурацией [Kr]4d¹⁰5s²5p² — это:",
        answers: ["Германий", "Олово", "Свинец", "Кремний"],
        correct: 1,
        hint: "[Kr]=36, + 10+2+2 = 50. Z=50 — это олово (Sn)."
    },
    {
        text: "Какой элемент является s-элементом?",
        answers: ["Алюминий (Al)", "Барий (Ba)", "Хлор (Cl)", "Железо (Fe)"],
        correct: 1,
        hint: "У бария последний электрон заполняет 6s-подуровень: [Xe]6s²."
    },

    // --- Тип 7: Изоэлектронные частицы ---
    {
        text: "Какие два иона имеют одинаковую электронную конфигурацию (изоэлектронны)? \nNa⁺, K⁺, Cl⁻, S²⁻, Ca²⁺",
        answers: ["Na⁺ и Cl⁻", "K⁺ и Cl⁻", "Na⁺ и Ca²⁺", "K⁺ и S²⁻"],
        correct: 0,
        hint: "Na⁺: 10 эл., Cl⁻: 18 эл., K⁺: 18 эл., Ca²⁺: 18 эл., S²⁻: 18 эл. Na⁺ НЕ изоэлектронен Cl⁻. Но K⁺, Cl⁻, S²⁻, Ca²⁺ — все имеют 18 электронов."
    },
    {
        text: "Какой атом изоэлектронен иону F⁻?",
        answers: ["Кислород (O)", "Неон (Ne)", "Хлор (Cl)", "Натрий (Na)"],
        correct: 1,
        hint: "F⁻ имеет 9+1=10 электронов. Неон тоже имеет 10 электронов."
    },
    {
        text: "Ион какого элемента имеет такую же электронную конфигурацию, как атом аргона (Ar)?",
        answers: ["Li⁺", "Na⁺", "K⁺", "Rb⁺"],
        correct: 2,
        hint: "Ar имеет 18 электронов. K⁺: 19-1=18 электронов."
    },

    // --- Тип 8: Правила заполнения (Клечковский, Хунд, Паули) ---
    {
        text: "Согласно правилу Клечковского, какой подуровень заполняется раньше?",
        answers: ["3d раньше 4s", "4s раньше 3d", "4p раньше 3d", "3d и 4s одновременно"],
        correct: 1,
        hint: "По правилу Клечковского: сумма (n+l) для 4s = 4+0 = 4, для 3d = 3+2 = 5. Меньшая сумма заполняется раньше."
    },
    {
        text: "Какое максимальное число электронов может находиться на d-подуровне?",
        answers: ["6", "10", "14", "2"],
        correct: 1,
        hint: "d-подуровень имеет 5 орбиталей, на каждой максимум 2 электрона: 5×2=10."
    },
    {
        text: "Согласно правилу Хунда, как заполняются 2p-орбитали у атома углерода?",
        answers: ["↑↓ ↑ _", "↑↓ _ _", "↑ ↑ _", "↑ _ _"],
        correct: 2,
        hint: "Правило Хунда: электроны занимают орбитали по одному с параллельными спинами, прежде чем спариваться."
    },
    {
        text: "Какое максимальное число электронов на 3-м энергетическом уровне?",
        answers: ["8", "18", "32", "2"],
        correct: 1,
        hint: "Максимальное число электронов на уровне n = 2n². Для n=3: 2×9 = 18."
    },
    {
        text: "Какое максимальное число электронов на f-подуровне?",
        answers: ["6", "10", "14", "18"],
        correct: 2,
        hint: "f-подуровень: 7 орбиталей × 2 = 14 электронов."
    },

    // --- Тип 9: Возбуждённое состояние ---
    {
        text: "Какая конфигурация соответствует возбуждённому состоянию атома углерода?",
        answers: ["1s²2s²2p²", "1s²2s¹2p³", "1s²2s²2p¹3s¹", "1s²2p⁴"],
        correct: 1,
        hint: "В возбуждённом состоянии 1 электрон с 2s переходит на 2p: 2s¹2p³."
    },
    {
        text: "В возбуждённом состоянии атом серы может образовать максимально валентность:",
        answers: ["2", "4", "6", "8"],
        correct: 2,
        hint: "В возбуждённом состоянии 3s²3p⁴ → 3s¹3p³3d², всего 6 неспаренных электронов."
    },
    {
        text: "Какой элемент НЕ может находиться в возбуждённом состоянии с расширением валентных возможностей?",
        answers: ["Сера (S)", "Фосфор (P)", "Кислород (O)", "Хлор (Cl)"],
        correct: 2,
        hint: "У кислорода нет d-подуровня на 2-м уровне, поэтому расширение невозможно."
    },

    // --- Тип 10: Конфигурация атомов конкретных элементов ---
    {
        text: "Сколько энергетических уровней у атома калия (K)?",
        answers: ["3", "4", "5", "2"],
        correct: 1,
        hint: "Калий в 4-м периоде, значит 4 энергетических уровня."
    },
    {
        text: "Сколько электронов на 2p-подуровне у атома фтора (F)?",
        answers: ["3", "4", "5", "6"],
        correct: 2,
        hint: "F: 1s²2s²2p⁵. На 2p — 5 электронов."
    },
    {
        text: "У какого элемента полностью заполнен 3d-подуровень в основном состоянии?",
        answers: ["Титан (Ti)", "Медь (Cu)", "Цинк (Zn)", "Никель (Ni)"],
        correct: 2,
        hint: "Zn: [Ar]3d¹⁰4s². У цинка 3d полностью заполнен (10 электронов)."
    },
    {
        text: "Какова электронная конфигурация атома кальция (Ca)?",
        answers: ["[Ar]3d²", "[Ar]4s²", "[Ar]4s¹", "[Ne]3s²3p⁶"],
        correct: 1,
        hint: "Ca (Z=20): 20 - 18(Ar) = 2 электрона на 4s."
    },
    {
        text: "Сколько полностью заполненных энергетических подуровней у атома алюминия (Al)?",
        answers: ["3", "4", "5", "2"],
        correct: 1,
        hint: "Al: 1s²(заполнен) 2s²(заполнен) 2p⁶(заполнен) 3s²(заполнен) 3p¹(не заполнен). Итого 4 полностью заполненных."
    },

    // --- Тип 11: Сравнение конфигураций ---
    {
        text: "Одинаковую конфигурацию внешнего уровня (ns²np⁵) имеют элементы:",
        answers: ["N и P", "O и S", "F и Cl", "C и Si"],
        correct: 2,
        hint: "ns²np⁵ — это VII группа, главная подгруппа: фтор (F) и хлор (Cl)."
    },
    {
        text: "У атомов кислорода и серы одинаковое:",
        answers: ["Число электронных уровней", "Число электронов на внешнем уровне", "Общее число электронов", "Число неспаренных электронов на p-подуровне"],
        correct: 1,
        hint: "O и S — в одной группе (VI), поэтому число внешних электронов одинаково: 6."
    },
    {
        text: "Какие два элемента имеют конфигурацию внешнего уровня ns²np²? \n1) C  2) N  3) Si  4) P  5) Ge",
        answers: ["1, 3 и 5", "2 и 4", "1 и 4", "3 и 4"],
        correct: 0,
        hint: "ns²np² — элементы IV группы: C(2s²2p²), Si(3s²3p²), Ge(4s²4p²)."
    },
];

// ===== TEST ENGINE =====
const TOTAL = questions.length;
let currentQuestion = 0;
let selectedAnswers = new Array(TOTAL).fill(null);
let questionStates = new Array(TOTAL).fill('unanswered');
questionStates[0] = 'current';
let answerLocked = false; // prevent clicking during feedback
let testFinished = false;

// Timer
let timerSeconds = 3000; // 50 min
const timerEl = document.getElementById('timer');
let timerInterval = setInterval(() => {
    timerSeconds--;
    if (timerSeconds < 0) { timerSeconds = 0; clearInterval(timerInterval); }
    const m = Math.floor(timerSeconds / 60);
    const s = timerSeconds % 60;
    timerEl.textContent = `${m}:${s.toString().padStart(2, '0')}`;
}, 1000);

// Build nav grid
function buildNavGrid() {
    const grid = document.getElementById('qGrid');
    grid.innerHTML = '';
    for (let i = 0; i < TOTAL; i++) {
        const div = document.createElement('div');
        div.className = 'q-num ' + questionStates[i];
        div.textContent = i + 1;
        div.onclick = () => goToQuestion(i + 1);
        grid.appendChild(div);
    }
}

function selectAnswer(el, idx) {
    if (answerLocked) return; // block during feedback
    if (questionStates[currentQuestion] === 'correct' || questionStates[currentQuestion] === 'wrong') return; // already answered
    document.querySelectorAll('.q-answer').forEach(a => {
        a.classList.remove('selected');
        a.classList.remove('correct-answer');
        a.classList.remove('wrong-answer');
    });
    el.classList.add('selected');
    selectedAnswers[currentQuestion] = idx;
}

function renderQuestion() {
    const q = questions[currentQuestion];
    document.getElementById('qCounter').textContent = `Вопрос ${currentQuestion + 1} из ${TOTAL}`;
    document.getElementById('questionText').innerHTML = q.text.replace(/\n/g, '<br>');

    // Context (if question has element row)
    document.getElementById('qContext').innerHTML = q.context ? `<div class="q-context">${q.context}</div>` : '';

    const container = document.getElementById('answersContainer');
    const letters = ['А', 'Б', 'В', 'Г'];
    container.innerHTML = q.answers.map((ans, i) =>
        `<div class="q-answer${selectedAnswers[currentQuestion] === i ? ' selected' : ''}" onclick="selectAnswer(this, ${i})">
            <div class="q-answer-letter">${letters[i]}</div>
            <div class="q-answer-text">${ans}</div>
        </div>`
    ).join('');

    // Button text
    const btn = document.getElementById('btnNext');
    if (currentQuestion === TOTAL - 1) {
        btn.textContent = '✅ Завершить тест';
    } else {
        btn.textContent = 'Следующий вопрос →';
    }

    buildNavGrid();
    updateStats();
}

function checkAnswer() {
    if (selectedAnswers[currentQuestion] !== null) {
        if (selectedAnswers[currentQuestion] === questions[currentQuestion].correct) {
            questionStates[currentQuestion] = 'correct';
        } else {
            questionStates[currentQuestion] = 'wrong';
        }
    }
}

function showAnswerFeedback(callback) {
    const sel = selectedAnswers[currentQuestion];
    const correct = questions[currentQuestion].correct;
    const answers = document.querySelectorAll('.q-answer');
    answerLocked = true;

    if (sel === correct) {
        // Correct!
        answers[sel].classList.remove('selected');
        answers[sel].classList.add('correct-answer');
        questionStates[currentQuestion] = 'correct';
        buildNavGrid();
        updateStats();
        setTimeout(() => { answerLocked = false; callback(); }, 800);
    } else {
        // Wrong — highlight wrong in red, correct in green
        answers[sel].classList.remove('selected');
        answers[sel].classList.add('wrong-answer');
        answers[correct].classList.add('correct-answer');
        questionStates[currentQuestion] = 'wrong';
        buildNavGrid();
        updateStats();
        setTimeout(() => { answerLocked = false; callback(); }, 1800);
    }
}

function nextQuestion() {
    if (answerLocked) return;

    if (selectedAnswers[currentQuestion] === null) {
        // Shake the answers container
        const container = document.getElementById('answersContainer');
        container.style.animation = 'none';
        container.offsetHeight; // force reflow
        container.style.animation = 'shake 0.4s ease';
        return;
    }

    // If already checked (user revisiting), just move on
    if (questionStates[currentQuestion] === 'correct' || questionStates[currentQuestion] === 'wrong') {
        moveToNext();
        return;
    }

    // Show feedback then advance
    showAnswerFeedback(() => {
        moveToNext();
    });
}

function moveToNext() {
    if (currentQuestion < TOTAL - 1) {
        currentQuestion++;
        if (questionStates[currentQuestion] === 'unanswered') {
            questionStates[currentQuestion] = 'current';
        }
        renderQuestion();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
        showResults();
    }
}

function goToQuestion(num) {
    if (answerLocked) return;
    if (selectedAnswers[currentQuestion] !== null && questionStates[currentQuestion] === 'current') {
        checkAnswer();
    } else if (questionStates[currentQuestion] === 'current') {
        questionStates[currentQuestion] = 'unanswered';
    }
    currentQuestion = num - 1;
    if (questionStates[currentQuestion] === 'unanswered') {
        questionStates[currentQuestion] = 'current';
    }
    renderQuestion();
}

function updateStats() {
    const correct = questionStates.filter(s => s === 'correct').length;
    const wrong = questionStates.filter(s => s === 'wrong').length;
    const answered = correct + wrong;
    const percent = answered > 0 ? Math.round((correct / answered) * 100) : 0;

    document.getElementById('progressPercent').textContent = `${percent}%`;
    document.getElementById('statAnswered').textContent = `${answered}/${TOTAL}`;
    document.getElementById('statCorrect').textContent = correct;
    document.getElementById('statWrong').textContent = wrong;

    const label = document.getElementById('progressLabel');
    if (percent >= 80) label.textContent = 'Отлично!';
    else if (percent >= 60) label.textContent = 'Хороший результат!';
    else if (percent >= 40) label.textContent = 'Можно лучше!';
    else if (answered > 0) label.textContent = 'Повторите теорию';
    else label.textContent = 'Начинаем!';
}

function showResults() {
    checkAnswer();
    testFinished = true;
    const correct = questionStates.filter(s => s === 'correct').length;
    const wrong = questionStates.filter(s => s === 'wrong').length;
    const unanswered = TOTAL - correct - wrong;
    const percent = Math.round((correct / TOTAL) * 100);

    document.getElementById('resultsScore').textContent = `${percent}%`;
    document.getElementById('resCorrect').textContent = correct;
    document.getElementById('resWrong').textContent = wrong + unanswered;

    const emoji = document.getElementById('resultsEmoji');
    const title = document.getElementById('resultsTitle');
    if (percent >= 90) { emoji.textContent = '🏆'; title.textContent = 'Превосходно!'; }
    else if (percent >= 70) { emoji.textContent = '🎉'; title.textContent = 'Отличный результат!'; }
    else if (percent >= 50) { emoji.textContent = '👍'; title.textContent = 'Неплохо!'; }
    else { emoji.textContent = '📚'; title.textContent = 'Нужно подучить теорию'; }

    document.getElementById('resultsOverlay').classList.add('show');
    // Update hint button
    document.querySelector('.q-hint').textContent = '💡 Показать подсказку';
    clearInterval(timerInterval);
    buildNavGrid();
    updateStats();
}

function restartTest() {
    currentQuestion = 0;
    selectedAnswers = new Array(TOTAL).fill(null);
    questionStates = new Array(TOTAL).fill('unanswered');
    questionStates[0] = 'current';
    answerLocked = false;
    testFinished = false;
    timerSeconds = 3000;
    timerInterval = setInterval(() => {
        timerSeconds--;
        if (timerSeconds < 0) { timerSeconds = 0; clearInterval(timerInterval); }
        const m = Math.floor(timerSeconds / 60);
        const s = timerSeconds % 60;
        timerEl.textContent = `${m}:${s.toString().padStart(2, '0')}`;
    }, 1000);
    document.querySelector('.q-hint').textContent = '💡 Подсказка (после теста)';
    document.getElementById('resultsOverlay').classList.remove('show');
    renderQuestion();
}

function showHint() {
    if (!testFinished) {
        alert("⏳ Подсказки доступны только после завершения теста!");
        return;
    }
    const q = questions[currentQuestion];
    alert("💡 Подсказка: " + (q.hint || "Вспомните правила заполнения электронных оболочек."));
}

// Initial render
buildNavGrid();
renderQuestion();
