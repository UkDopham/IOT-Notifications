import React, {useEffect, useState, Fragment } from 'react';
import { Avatar, Box, Typography, List, ListItem } from '@material-ui/core';
import {useStyles} from './Notifications.style';
import axios, {AxiosResponse} from 'axios';
import {API} from '../Utils/Api';

export interface INotification {
  text:string;
  subtext:string;
}


type Props = {
  notification: INotification;
}

export const ProjectDetail = (props: Props) => {
  const notification = props.notification;
  const classes = useStyles();

  useEffect(() => {
    // Use [] as second argument in useEffect for not rendering each time
    axios.get('http://localhost:8080/')
    .then((response: AxiosResponse) => {
        console.log(response.data);
    });
}, []);

  return (
    <List className={classes.list}>
      <ListItem>
        <Typography className={classes.text}>{notification.text}</Typography>
      </ListItem>
      <ListItem>
        <Typography className={classes.subtext}>{notification.subtext}</Typography>
      </ListItem>
    </List>
  );
}