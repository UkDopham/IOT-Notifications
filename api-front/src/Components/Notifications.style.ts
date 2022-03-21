import { makeStyles, createStyles } from '@material-ui/core/styles';
import { Theme } from '@material-ui/core';

export const useStyles = makeStyles<Theme>(theme => //cursive
(
  {
    text: {
      height: 200,
    },
  })
);