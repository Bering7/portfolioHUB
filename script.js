document.addEventListener("DOMContentLoaded", () => {
  const header = document.getElementById("header");
  const navToggle = document.getElementById("navToggle");
  const navMenu = document.getElementById("navMenu");
  const navLinks = document.querySelectorAll(".nav__link");
  const sections = document.querySelectorAll("main section[id]");

  /* ---------- Menu mobile ---------- */
  const closeMenu = () => {
    navMenu.classList.remove("is-open");
    navToggle.classList.remove("is-open");
    navToggle.setAttribute("aria-expanded", "false");
    navToggle.setAttribute("aria-label", "Abrir menu");
    document.body.classList.remove("no-scroll");
  };

  navToggle.addEventListener("click", () => {
    const isOpen = navMenu.classList.toggle("is-open");
    navToggle.classList.toggle("is-open", isOpen);
    navToggle.setAttribute("aria-expanded", String(isOpen));
    navToggle.setAttribute("aria-label", isOpen ? "Fechar menu" : "Abrir menu");
    document.body.classList.toggle("no-scroll", isOpen);
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeMenu();
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 768) closeMenu();
  });

  /* ---------- Rolagem suave com compensação do header ---------- */
  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (e) => {
      const id = link.getAttribute("href");
      if (id.length < 2) return;

      const target = document.querySelector(id);
      if (!target) return;

      e.preventDefault();
      closeMenu();

      const offset = id === "#inicio" ? 0 : target.offsetTop - header.offsetHeight + 1;
      window.scrollTo({ top: offset, behavior: "smooth" });
      history.replaceState(null, "", id);
    });
  });

  /* ---------- Sombra no header + link ativo ---------- */
  const onScroll = () => {
    header.classList.toggle("is-scrolled", window.scrollY > 10);

    const position = window.scrollY + header.offsetHeight + window.innerHeight * 0.25;
    let current = "";

    sections.forEach((section) => {
      if (position >= section.offsetTop) current = section.id;
    });

    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 4) {
      current = sections[sections.length - 1].id;
    }

    navLinks.forEach((link) => {
      link.classList.toggle("is-active", link.getAttribute("href") === `#${current}`);
    });
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Animação de entrada discreta ---------- */
  const revealItems = document.querySelectorAll(
    ".section__header, .about__grid, .skills__group, .card"
  );

  if ("IntersectionObserver" in window) {
    revealItems.forEach((el) => el.classList.add("reveal"));

    const observer = new IntersectionObserver(
      (entries, obs) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            obs.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );

    revealItems.forEach((el) => observer.observe(el));
  }

  /* ---------- Ano no rodapé ---------- */
  document.getElementById("year").textContent = new Date().getFullYear();

  /* ---------- Alternador de Tema (Modo Escuro / Claro) ---------- */
  const themeToggle = document.getElementById("themeToggle");
  if (themeToggle) {
    themeToggle.addEventListener("click", () => {
      const currentTheme = document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light";
      const newTheme = currentTheme === "dark" ? "light" : "dark";

      document.documentElement.setAttribute("data-theme", newTheme);
      localStorage.setItem("theme", newTheme);
    });
  }

  /* ---------- Dicionário e Suporte Bilíngue (PT / EN) ---------- */
  const translations = {
    pt: {
      page_title: "Henrique Moura Bering",
      meta_description: "Henrique Bering — Ciência de Dados & Machine Learning. Portfólio, projetos e contato.",
      nav_about: "Sobre",
      nav_skills: "Skills",
      nav_projects: "Projetos",
      hero_eyebrow: "Disponível para estágio",
      hero_subtitle: "Ciência de Dados & Machine Learning",
      hero_text: "Python, SQL, Power BI e análise de dados aplicados a problemas reais: automação de processos, análise exploratória, aplicações interativas e criação de dashboards.",
      contact_email: "E-mail",
      contact_whatsapp: "WhatsApp",
      contact_github: "GitHub",
      contact_linkedin: "LinkedIn",
      resume_pt: "Currículo - PT",
      resume_en: "Currículo - EN",
      about_title: "Sobre",
      about_text: "Estudante do 2º semestre no UniCEUB. Base sólida em Python e análise de dados. Busco oportunidade de estágio para aplicar habilidades técnicas na geração de insights orientados a dados e no desenvolvimento de aplicações.",
      fact_education_label: "Formação",
      fact_education_val: "Ciência de Dados e Machine Learning — UniCEUB",
      fact_term_label: "Período",
      fact_term_val: "2º semestre",
      fact_model_label: "Modalidade",
      fact_model_val: "Presencial, híbrido ou remoto",
      fact_location_label: "Localização",
      fact_location_val: "Brasília — DF",
      skills_title: "Skills",
      skills_group_languages: "Linguagens & Dados",
      skills_group_platforms: "Plataformas & Visualização",
      skills_group_tools: "Ferramentas",
      badge_oop: "POO",
      projects_title: "Projetos",
      project_1_title: "Integração e Automação de Processos",
      project_1_text: "Integração de banco de dados Supabase/PostgreSQL via API REST e disparo automatizado de mensagens pela Z-API, reduzindo etapas manuais no fluxo de comunicação.",
      project_1_aria: "Ver repositório do projeto Integração e Automação de Processos no GitHub",
      project_2_title: "Controle Térmico de Satélites",
      project_2_text: "Simulação do comportamento térmico de um satélite em órbita baixa (LEO) e análise dos dados de temperatura gerados ao longo das órbitas.",
      project_2_aria: "Ver repositório do projeto Controle Térmico de Satélites no GitHub",
      tag_simulation: "Simulação",
      tag_data_analysis: "Análise de Dados",
      project_3_title: "Análise de Crédito e Cancelamento (Churn)",
      project_3_text: "Análise exploratória de uma base de clientes de crédito para identificar os padrões e variáveis mais associados ao cancelamento.",
      project_3_aria: "Ver repositório do projeto Análise de Crédito e Cancelamento (Churn) no GitHub",
      tag_visualization: "Visualização",
      project_4_title: "Assistente Virtual com IA",
      project_4_text: "Chatbot interativo com interface web construída em Streamlit, integrando um modelo de linguagem para responder às perguntas do usuário.",
      project_4_aria: "Ver repositório do projeto Assistente Virtual com IA no GitHub",
      tag_ai: "IA",
      back_to_top: "Voltar ao topo ↑",
      theme_toggle_label: "Alternar modo escuro e claro",
      nav_toggle_open: "Abrir menu",
      nav_toggle_close: "Fechar menu"
    },
    en: {
      page_title: "Henrique Moura Bering | Portfolio",
      meta_description: "Henrique Bering — Data Science & Machine Learning. Portfolio, projects, and contact.",
      nav_about: "About",
      nav_skills: "Skills",
      nav_projects: "Projects",
      hero_eyebrow: "Available for internship",
      hero_subtitle: "Data Science & Machine Learning",
      hero_text: "Python, SQL, Power BI, and data analysis applied to real-world challenges: process automation, exploratory analysis, interactive applications, and dashboard design.",
      contact_email: "Email",
      contact_whatsapp: "WhatsApp",
      contact_github: "GitHub",
      contact_linkedin: "LinkedIn",
      resume_pt: "Resume - PT",
      resume_en: "Resume - EN",
      about_title: "About",
      about_text: "2nd-semester student at UniCEUB with a solid foundation in Python and data analysis. Seeking an internship opportunity to apply technical skills in generating data-driven insights and developing practical applications.",
      fact_education_label: "Education",
      fact_education_val: "Data Science and Machine Learning — UniCEUB",
      fact_term_label: "Term",
      fact_term_val: "2nd semester",
      fact_model_label: "Work Model",
      fact_model_val: "On-site, hybrid, or remote",
      fact_location_label: "Location",
      fact_location_val: "Brasília — DF, Brazil",
      skills_title: "Skills",
      skills_group_languages: "Languages & Data",
      skills_group_platforms: "Platforms & Visualization",
      skills_group_tools: "Tools",
      badge_oop: "OOP",
      projects_title: "Projects",
      project_1_title: "Process Integration and Automation",
      project_1_text: "Integration of Supabase/PostgreSQL database via REST API and automated messaging via Z-API, reducing manual steps in the communication workflow.",
      project_1_aria: "View Integration and Process Automation repository on GitHub",
      project_2_title: "Satellite Thermal Control",
      project_2_text: "Thermal behavior simulation of a satellite in low Earth orbit (LEO) and temperature data analysis generated across orbits.",
      project_2_aria: "View Satellite Thermal Control repository on GitHub",
      tag_simulation: "Simulation",
      tag_data_analysis: "Data Analysis",
      project_3_title: "Credit Analysis and Churn Prediction",
      project_3_text: "Exploratory data analysis (EDA) of a credit customer base to identify key patterns and drivers associated with churn.",
      project_3_aria: "View Credit Analysis and Churn Prediction repository on GitHub",
      tag_visualization: "Visualization",
      project_4_title: "AI Virtual Assistant",
      project_4_text: "Interactive chatbot with web UI built with Streamlit, integrating a large language model to answer user queries.",
      project_4_aria: "View AI Virtual Assistant repository on GitHub",
      tag_ai: "AI",
      back_to_top: "Back to top ↑",
      theme_toggle_label: "Toggle dark and light mode",
      nav_toggle_open: "Open menu",
      nav_toggle_close: "Close menu"
    }
  };

  const applyLanguage = (lang) => {
    const dict = translations[lang] || translations.pt;

    document.documentElement.lang = lang === "pt" ? "pt-BR" : "en";

    if (dict.page_title) document.title = dict.page_title;
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc && dict.meta_description) metaDesc.setAttribute("content", dict.meta_description);

    document.querySelectorAll("[data-i18n]").forEach((el) => {
      const key = el.getAttribute("data-i18n");
      if (dict[key]) el.textContent = dict[key];
    });

    document.querySelectorAll("[data-i18n-aria]").forEach((el) => {
      const key = el.getAttribute("data-i18n-aria");
      if (dict[key]) el.setAttribute("aria-label", dict[key]);
    });

    const btnPt = document.getElementById("langPt");
    const btnEn = document.getElementById("langEn");
    if (btnPt && btnEn) {
      const isPt = lang === "pt";
      btnPt.classList.toggle("is-active", isPt);
      btnPt.setAttribute("aria-pressed", String(isPt));
      btnEn.classList.toggle("is-active", !isPt);
      btnEn.setAttribute("aria-pressed", String(!isPt));
    }

    const themeBtn = document.getElementById("themeToggle");
    if (themeBtn && dict.theme_toggle_label) {
      themeBtn.setAttribute("aria-label", dict.theme_toggle_label);
      themeBtn.setAttribute("title", dict.theme_toggle_label);
    }

    if (navToggle) {
      const isOpen = navMenu.classList.contains("is-open");
      navToggle.setAttribute("aria-label", isOpen ? dict.nav_toggle_close : dict.nav_toggle_open);
    }

    localStorage.setItem("lang", lang);
  };

  const langButtons = document.querySelectorAll(".lang-btn");
  langButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const targetLang = btn.getAttribute("data-lang");
      if (targetLang) applyLanguage(targetLang);
    });
  });

  const initialLang = localStorage.getItem("lang") || "pt";
  applyLanguage(initialLang);
});

