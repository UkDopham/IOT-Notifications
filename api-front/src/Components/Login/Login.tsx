import { useEffect, useState } from 'react';
import { Box, Typography, List, ListItem, Button, TextField } from '@material-ui/core';
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
        axios.post(baseURL, {
            data: {
                email: currentAccount.email,
                password: currentAccount.password,
            }
        }) //Modifier en fonction du chemin de la requete
            .then((response: AxiosResponse) => {
                console.log(response.data);
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
        <List className={classes.box}>
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
                <Button className={classes.buttonSmall} onClick={() => Login()}>
                    <Typography className={classes.text}>Login</Typography>
                </Button>
            </ListItem>
        </List>
    );
}