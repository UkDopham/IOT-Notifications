import { useEffect, useState } from 'react';
import { Box, Typography, List, ListItem, Button, TextField, Avatar } from '@material-ui/core';
import { useStyles } from './Login.style';
import axios, { AxiosResponse } from 'axios';
import { API, baseURL } from '../../Utils/Api';

export interface IAccount {
    email: string;
    password: string;
}

type Props = {
    setIsLog: any,
}

export const Login = (props: Props) => {
    const [currentAccount, setCurrentAccount] = useState({
        email: "",
        password: "",
    })
    const classes = useStyles();

    const PostAccount = () => {
        const data={email: currentAccount.email,password: currentAccount.password};
        //POST méthode à utiliser pour communiquer avec le BACKEND - Valentin
        // fetch(API.postAccount,{
        //     method:'POST',
        //     mode:'no-cors',
        //     headers: {'Content-Type':'application/json'},
        //     body : JSON.stringify(data)
        // })
            
         //Modifier en fonction du chemin de la requete
        axios.post(API.postLogin, {
            data: {
                email: currentAccount.email,
                password: currentAccount.password,
            }
        }) //Modifier en fonction du chemin de la requete
              .then((response: AxiosResponse) => {
                console.log(response);
                console.log("post " + currentAccount.email);
                props.setIsLog(true);
            }).catch((axios: any) => {
                console.log(axios); // Pas le bon mot de passe
            });
    }

    const Login = () => {
        console.log("login " + currentAccount.email + " " + currentAccount.password);
        props.setIsLog(true); //DEBUG
        //PostAccount();
    }

    return (
        <Box>
            <List className={classes.box}>
                <ListItem className={classes.listItem}>
                    <Avatar className={classes.avatar} src="serveur.png" />
                    <Typography className={classes.title} >SmartHome</Typography>
                    <Typography className={classes.subtitle} >by Bento</Typography>
                </ListItem>
                <ListItem className={classes.listItem}>
                    <Typography className={classes.text} >Email :</Typography>
                    <TextField className={classes.text}
                        value={currentAccount.email}
                        id="accountname"
                        onChange={(event) => setCurrentAccount({
                            email: event.target.value,
                            password: currentAccount.password,
                        })}
                    />
                </ListItem>

                <ListItem className={classes.listItem}>
                    <Typography className={classes.text} >Password :</Typography>
                    <TextField className={classes.text}
                        type="password"
                        value={currentAccount.password}
                        id="accountemail"
                        onChange={(event) => setCurrentAccount({
                            email: currentAccount.email,
                            password: event.target.value,
                        })}
                    />
                </ListItem>

                <ListItem className={classes.listItem}>
                    <Button className={classes.buttonSmall} onClick={() => PostAccount()}>
                        <Typography className={classes.text}>Login</Typography>
                    </Button>
                </ListItem>
            </List>
        </Box>
    );
}