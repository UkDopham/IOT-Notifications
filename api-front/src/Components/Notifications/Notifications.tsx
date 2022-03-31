import { useEffect, useState } from 'react';
import { Box, Typography, List, ListItem, Button, TextField } from '@material-ui/core';
import { useStyles } from './Notifications.style';
import axios, { AxiosResponse } from 'axios';
import { API, baseURL } from '../../Utils/Api';

const privateKey = "";
const publicKey = "";

let publicKeyBack = "";
export interface INotification {
  text: string;
  subtext: string;
}

export interface IAccount {
  name: string;
  email: string;
  phone: string;
  id: number;
}

const test = [{
  name: "John",
  email: "John@gmail.com",
  phone: "1",
  id: 1,
},
{
  name: "Mike",
  email: "Mike@gmail.com",
  phone: "2",
  id: 2,
}]

type Props = {
  setIsLog: any,
}

export const Notifications = (props: Props) => {
  const [accounts, setAccounts] = useState(test);
  const [currentAccount, setCurrentAccount] = useState({
    name: "",
    email: "",
    phone: "",
    id: -1,
  })
  const classes = useStyles();

  useEffect(() => {
    // Use [] as second argument in useEffect for not rendering each time
    //GetAllAccounts();
  }, []);

  const GetAllAccounts = () => {
    axios.get(baseURL) //Modifier en fonction du chemin de la requete
      .then((response: AxiosResponse) => {
        console.log(response.data);
        setAccounts(response.data);
      }).catch((axios: any) => {
        console.log(axios);
      });
  }

  const PostPublicKey = () => {
    axios.post(baseURL, {
      data: {
        publicKey: publicKey
      }
    }) //Modifier en fonction du chemin de la requete
      .then((response: AxiosResponse) => {
        console.log(response.data);
        publicKeyBack = response.data;
      }).catch((axios: any) => {
        console.log(axios);
      });
  }

  const PostAccount = (account: IAccount) => {
    axios.post(baseURL, {
      data: {
        name: account.name,
        email: account.email,
        phone: account.phone,
        id: account.id
      }
    }) //Modifier en fonction du chemin de la requete
      .then((response: AxiosResponse) => {
        console.log(response.data);
        console.log("post " + account.id);
        account.id = response.data; // on recup l'id de la reponse
        accounts.push(account);
        accounts.sort((accountA, accountB) => accountA.id > accountB.id ? 1 : -1);
        setCurrentAccount({
          name: "",
          email: "",
          phone: "",
          id: -1,
        });
      }).catch((axios: any) => {
        console.log(axios);
      });
  }

  const PutAccount = (account: IAccount) => {
    axios.put(baseURL, {
      data: {
        name: account.name,
        email: account.email,
        phone: account.phone,
        id: account.id
      }
    }) //Modifier en fonction du chemin de la requete
      .then((response: AxiosResponse) => {
        console.log(response.data);
        console.log("put " + account.id);
      }).catch((axios: any) => {
        console.log(axios);
      });
  }

  const DeleteAccount = (id: number) => {
    axios.delete(baseURL, { data: { id: id } }) //Modifier en fonction du chemin de la requete
      .then((response: AxiosResponse) => {
        console.log(response.data);
        console.log("delete " + id);

        const newList = accounts.filter((account) => account.id !== id);
        setAccounts(newList);
      }).catch((axios: any) => {
        console.log(axios);
      });
  }

  const OnClickAddNew = () => {
    console.log("add new contact " + currentAccount.id);
    //PostAccount(currentAccount);
  }

  const OnClickDelete = (id: number) => {
    console.log("on click delete " + id);
    //DeleteAccount(id);
  }

  const OnChangePut = (account: IAccount) => {
    console.log("on change put " + account.id);
    console.log(account.name);
    //PutAccount(account);
  }

  const OnChangeName = (id: number, name: any) => {
    const account: any = accounts.find((account) => account.id === id);
    const newAccount = {
      name: name,
      email: account.email,
      phone: account.phone,
      id: account.id,
    }
    const newList = accounts.filter((account) => account.id !== id);
    newList.push(newAccount);
    newList.sort((accountA, accountB) => accountA.id > accountB.id ? 1 : -1);
    setAccounts(newList);
    OnChangePut(newAccount);
  }

  const OnChangeEmail = (id: number, email: any) => {
    const account: any = accounts.find((account) => account.id === id);
    const newAccount = {
      name: account.name,
      email: email,
      phone: account.phone,
      id: account.id,
    }
    const newList = accounts.filter((account) => account.id !== id);
    newList.push(newAccount);
    newList.sort((accountA, accountB) => accountA.id > accountB.id ? 1 : -1);
    setAccounts(newList);
    OnChangePut(newAccount);
  }

  const OnChangePhone = (id: number, phone: any) => {
    const account: any = accounts.find((account) => account.id === id);
    const newAccount = {
      name: account.name,
      email: account.email,
      phone: phone,
      id: account.id,
    }
    const newList = accounts.filter((account) => account.id !== id);
    newList.push(newAccount);
    newList.sort((accountA, accountB) => accountA.id > accountB.id ? 1 : -1);
    setAccounts(newList);
    OnChangePut(newAccount);
  }

  return (
    <Box>
      <ListItem>
        <Typography className={classes.text} >Name :</Typography>
        <TextField className={classes.text}
          value={currentAccount.name}
          id="accountname"
          onChange={(event) => setCurrentAccount({
            name: event.target.value,
            email: currentAccount.email,
            phone: currentAccount.phone,
            id: -1,
          })}
        />

        <Typography className={classes.text} >Email :</Typography>
        <TextField className={classes.text}
          value={currentAccount.email}
          id="accountemail"
          onChange={(event) => setCurrentAccount({
            name: currentAccount.name,
            email: event.target.value,
            phone: currentAccount.phone,
            id: -1,
          })}
        />

        <Typography className={classes.text} >Phone number :</Typography>
        <TextField className={classes.text}
          value={currentAccount.phone}
          id="accountphone"
          onChange={(event) => setCurrentAccount({
            name: currentAccount.name,
            email: currentAccount.email,
            phone: event.target.value,
            id: -1,
          })}
        />

        <Button className={classes.buttonSmall} onClick={() => OnClickAddNew()}>
          <Typography >Create new contact</Typography>
        </Button>
      </ListItem>
      <List className={classes.list}><ListItem>
      </ListItem>
        {accounts.map(
          (account: IAccount) =>
            <ListItem key={account.id}>
              <Typography className={classes.text} >Name :</Typography>
              <TextField className={classes.text}
                value={account.name}
                id="accountname"
                onChange={(event) => OnChangeName(account.id, event.target.value)}
              />

              <Typography className={classes.text} >Email :</Typography>
              <TextField className={classes.text}
                value={account.email}
                id="accountemail"
                onChange={(event) => OnChangeEmail(account.id, event.target.value)}
              />

              <Typography className={classes.text} >Phone number :</Typography>
              <TextField className={classes.text}
                value={account.phone}
                id="accountphone"
                onChange={(event) => OnChangePhone(account.id, event.target.value)}
              />

              <Button className={classes.buttonSmall} onClick={() => OnClickDelete(account.id)}>
                <Typography >Delete</Typography>
              </Button>
            </ListItem>
        )
        }
      </List>
    </Box>
  );
}