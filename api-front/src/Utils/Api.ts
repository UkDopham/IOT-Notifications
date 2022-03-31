export const baseURL = "http://localhost:8080/";

export const API = {  
    post : baseURL + "api/post",
    postAccount :  baseURL + "api/post/newAccount", // Création d'un compte
    getAccounts : baseURL + "api/get/allAccounts", // Récupération des comptes existants
    deleteAccount: baseURL + "api/delete", // Suppression d'un compte
    putAccount: baseURL + "api/put/changeAccount", // Modification d'un compte
    postLogin: baseURL + "api/post/login", // Connexion d'un compte
}