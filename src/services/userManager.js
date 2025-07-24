class UserManager {
  constructor() {
    this.usuarios = [];
  }

  cadastrarUsuario(user) {
    this.usuarios.push(user);
  }

  fazerLogin(email, senha) {
    return this.usuarios.some(u => u.email === email && u.senha === senha);
  }

  recuperarSenha(email) {
    const user = this.usuarios.find(u => u.email === email);
    return user ? user.senha : null;
  }

  listarUsuarios() {
    return this.usuarios;
  }
}

module.exports = UserManager;
