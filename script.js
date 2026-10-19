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
    ".section__header, .about__grid, .stack__subtitle, .stack-cloud, .portfolio-row, .contact__intro, .contact__list"
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
      nav_skills: "Stack",
      nav_projects: "Projetos",
      nav_contact: "Contato",
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
      skills_title: "Stack",
      stack_subtitle: "Ferramentas que utilizo",
      badge_oop: "POO",
      projects_title: "Projetos",
      project_1_title: "Integração e Automação de Processos",
      project_1_text: "Integração de banco de dados Supabase/PostgreSQL via API REST e disparo automatizado de mensagens pela Z-API.",
      project_2_title: "Controle Térmico de Satélites",
      project_2_text: "Simulação térmica em órbita baixa (LEO) e análise de dados de temperatura gerados ao longo das órbitas.",
      project_3_title: "Análise de Crédito e Cancelamento (Churn)",
      project_3_text: "Análise exploratória de uma base de clientes de crédito para identificar padrões de cancelamento.",
      project_4_title: "Assistente Virtual com IA",
      project_4_text: "Chatbot interativo com interface web construída em Streamlit, integrando um modelo de linguagem.",
      project_5_title: "Monitor Financeiro",
      project_5_text: "Aplicação web com Supabase (Auth + PostgreSQL), Chart.js e CRUD de transações.",
      contact_title: "Vamos conversar",
      contact_text: "Estou aberto a oportunidades de contratação ou apenas para trocar uma ideia sobre programação e dados.",
      contact_phone_label: "Telefone / WhatsApp",
      back_to_top: "Voltar ao topo ↑",
      theme_toggle_label: "Alternar modo escuro e claro",
      nav_toggle_open: "Abrir menu",
      nav_toggle_close: "Fechar menu",
      footer_location: "Brasília, DF",
      github_btn: "VER NO GITHUB"
    },
    en: {
      page_title: "Henrique Moura Bering | Portfolio",
      meta_description: "Henrique Bering — Data Science & Machine Learning. Portfolio, projects, and contact.",
      nav_about: "About",
      nav_skills: "Stack",
      nav_projects: "Projects",
      nav_contact: "Contact",
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
      fact_location_val: "Brasília, Brazil",
      skills_title: "Stack",
      stack_subtitle: "Tools I work with",
      badge_oop: "OOP",
      projects_title: "Projects",
      project_1_title: "Process Integration and Automation",
      project_1_text: "Integration of Supabase/PostgreSQL database via REST API and automated messaging via Z-API.",
      project_2_title: "Satellite Thermal Control",
      project_2_text: "Thermal simulation in low Earth orbit (LEO) and analysis of temperature data generated across orbits.",
      project_3_title: "Credit Analysis and Churn",
      project_3_text: "Exploratory analysis of a credit customer base to identify cancellation patterns.",
      project_4_title: "AI Virtual Assistant",
      project_4_text: "Interactive chatbot with a web interface built in Streamlit, integrating a language model.",
      project_5_title: "Financial Monitor",
      project_5_text: "Web application with Supabase (Auth + PostgreSQL), Chart.js, and transaction CRUD.",
      contact_title: "Let's talk",
      contact_text: "I'm open to hiring opportunities or simply chatting about programming and data.",
      contact_phone_label: "Phone / WhatsApp",
      back_to_top: "Back to top ↑",
      theme_toggle_label: "Toggle dark and light mode",
      nav_toggle_open: "Open menu",
      nav_toggle_close: "Close menu",
      footer_location: "Brasília, Brazil",
      github_btn: "VIEW ON GITHUB"
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

    const langToggleBtn = document.getElementById("langToggle");
    if (langToggleBtn) {
      const nextLang = lang === "pt" ? "en" : "pt";
      langToggleBtn.textContent = nextLang.toUpperCase();
      const label = lang === "pt" ? "Mudar para inglês / Switch to English" : "Mudar para português / Switch to Portuguese";
      langToggleBtn.setAttribute("aria-label", label);
      langToggleBtn.setAttribute("title", label);
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

  const langToggleBtn = document.getElementById("langToggle");
  if (langToggleBtn) {
    langToggleBtn.addEventListener("click", () => {
      const currentLang = localStorage.getItem("lang") || (document.documentElement.lang.startsWith("pt") ? "pt" : "en");
      const nextLang = currentLang === "pt" ? "en" : "pt";
      applyLanguage(nextLang);
    });
  }

  const initialLang = localStorage.getItem("lang") || "pt";
  applyLanguage(initialLang);
});

