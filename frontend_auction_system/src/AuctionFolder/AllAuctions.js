import { Grid, ListItem, Paper, Switch } from '@mui/material';
import React, { useState } from 'react';


 function FullWidthGrid() {
	const [spacing, setSpacing] = useState(2)

	return (
		<div>
            <Grid container spacing={2}>
  <Grid item xs={6} md={8}>
    <ListItem>xs=6 md=8</ListItem>
  </Grid>
  <Grid item xs={6} md={4}>
    <ListItem>xs=6 md=4</ListItem>
    
  </Grid>
  <Grid item xs={6} md={4}>
    <ListItem>xs=6 md=4</ListItem>
  </Grid>
  <Grid item xs={6} md={8}>
    <ListItem>xs=6 md=8</ListItem>
  </Grid>
</Grid>
			<Switch onChange=
			{() => setSpacing(spacing => spacing === 2 ? 4 : 2)} />
			Spacing {spacing}px
			<div>
				<Grid container spacing={spacing}>
					<Grid item>
						<Paper sx={{
							height: 140,
							width: 100,
							border: '2px solid black'
						}}></Paper>
					</Grid>
					<Grid item>
						<Paper sx={{
							height: 140,
							width: 100,
							border: '2px solid black'
						}}></Paper>
					</Grid>
				</Grid>
			</div>
		</div>
	);
}
export default FullWidthGrid;