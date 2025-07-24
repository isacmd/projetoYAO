class User {
  constructor(nome, telefone, dataNasc, cpf, email, senha) {
    this.nome = nome;
    this.telefone = telefone;
    this.dataNasc = dataNasc;
    this.cpf = cpf;
    this.email = email;
    this.senha = senha;
  }

  toString() {
    return `Nome: ${this.nome}, Email: ${this.email}, Telefone: ${this.telefone}`;
  }
}

module.exports = User;
