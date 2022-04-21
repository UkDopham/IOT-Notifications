import { makeStyles} from '@material-ui/core/styles';
import { Theme } from '@material-ui/core';

export const useStyles = makeStyles<Theme>(theme => 
(
  {
    text: {
      margin: 10,
      padding: 5,
      backgroundColor: "#94ce98",
      fontSize: 15,
      minWidth: 100,
      maxWidth: 200,
      borderRadius: 10,
      color :"white",
      fontWeight : "bold"
    },
    buttonBig: {
      margin: 15,
      padding: 10,
      backgroundColor: "blue",
    },
    buttonSmall:{
      margin: 10,
      padding: 5,
      backgroundColor: "#477e5e",
      color :"white"
    },
    input:{
      color :"white"
    }
  })
);