class User {
  login;
  email;
  password;

  constructor(login, email, password) {
    login = login;
    email = email;
    password = password;
  }

  static getAllUsers() {
    const fs = require("fs");
    const userListJSON = JSON.stringify(userList);

    // Запись JSON-строки в файл
    fs.writeFile("users.json", userListJSON, "utf8", (err) => {
      if (err) {
        console.error("Ошибка при записи в файл:", err);
        return;
      }
      console.log("Список классов user успешно записан в файл users.json");
    });
  }
  addtojsondb() {}
}
// $("#RegForm").submit(function (event) {
//   event.preventDefault();
//   // Предотвращает отправку формы по умолчанию

//   // Получение значений полей формы
//   let login = $("input[name='Login']").val();
//   let email = $("input[name='email']").val();
//   let password1 = $("input[name='password1']").val();
//   let password2 = $("input[name='password2']").val();

//   // Обработка данных формы

//   if (password1 != password2 || password1 == "") {
//     alert("Somthing is not right");
//     return;
//   }

//   let user = new User();
//   user.login = login;
//   user.email = email;
//   user.password = password1;

//   console.log(
//     "login\n" +
//       login +
//       "Email\n" +
//       email +
//       "password1\n" +
//       password1 +
//       "password2\n" +
//       password2
//   );

//   $("#RegForm")[0].reset();
// });

$("#Logbtn").click(function (e) {
  $("#RegForm").css({
    display: "none",
  });
  $("#LogForm").css({
    display: "flex",
  });
  console.log("log");

  let content = "text";
});

$("#Regbtn").click(function (e) {
  $("#RegForm").css({
    display: "flex",
  });
  $("#LogForm").css({
    display: "none",
  });
  console.log("reg");
});
