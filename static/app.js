function toggleChat() {
  const panel = document.getElementById("kcx-ai-panel");
  panel.style.display = panel.style.display === "flex" ? "none" : "flex";
}

function addMsg(text, type) {
  const body = document.getElementById("kcx-ai-body");

  const div = document.createElement("div");
  div.innerText = text;
  div.style.margin = "8px 0";
  div.style.padding = "8px";
  div.style.borderRadius = "8px";
  div.style.maxWidth = "85%";
  div.style.whiteSpace = "pre-wrap";

  if (type === "user") {
    div.style.background = "#111";
    div.style.color = "white";
    div.style.marginLeft = "auto";
  } else {
    div.style.background = "#f1f1f1";
    div.style.color = "#111";
    div.style.marginRight = "auto";
  }

  body.appendChild(div);
  body.scrollTop = body.scrollHeight;
}

async function sendMsg() {
  const input = document.getElementById("kcx-input");
  const question = input.value.trim();

  if (!question) return;

  addMsg(question, "user");

  input.value = "";
  input.style.height = "42px";

  addMsg("Yazıyor...", "ai");

  try {
    const res = await fetch("/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        question: question,
        level: "beginner"
      })
    });

    const data = await res.json();

    const body = document.getElementById("kcx-ai-body");
    if (body.lastChild) {
      body.lastChild.remove();
    }

    if (!res.ok) {
      addMsg(data.message || "Bir hata oluştu. Lütfen tekrar dene.", "ai");
      return;
    }

    addMsg(data.message || "Yanıt alınamadı.", "ai");

  } catch (error) {
    const body = document.getElementById("kcx-ai-body");
    if (body.lastChild) {
      body.lastChild.remove();
    }

    addMsg("Bağlantı hatası oluştu. Lütfen tekrar dene.", "ai");
    console.error(error);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("kcx-input");

  if (input) {
    input.addEventListener("keydown", function (event) {
      if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendMsg();
      }
    });
  }
});
