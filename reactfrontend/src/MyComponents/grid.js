import GridLayout from "react-grid-layout";
import styled from "styled-components";




const layout = [
  { i: "blue-eyes-dragon", x: 0, y: 0, w: 1, h: 1 },
  { i: "dark-magician", x: 1, y: 0, w: 1, h: 1 },
  { i: "kuriboh", x: 2, y: 0, w: 1, h: 1 },
  { i: "spell-caster", x: 3, y: 0, w: 1, h: 1 },

];

const GridItemWrapper = styled.div`
  background: Teal;
`;

const GridItemContent = styled.div`
  padding: 8px;
  color: white;
`;

const Root = styled.div`
  padding: 16px;
`;

export const Grid = () => {
  return (
    <Root>
      <GridLayout layout={layout} cols={5} rowHeight={350} width={1500}>
        <GridItemWrapper key="blue-eyes-dragon">
          <GridItemContent>SmartPhone
            <center>
            <div><img src="https://m.media-amazon.com/images/I/71AvQd3VzqL._SX385_.jpg" alt="" height="150px" width="150px"/></div>
            Name:OnePlus Nord
            <div>Description: 128GB Rom, 8GB ram, Super Amoled Display</div>
            <div>Manufacture Year: 2021</div>
            <div>Base Price:22,499</div>
            <div>Owner: Rohan J.</div>
            </center>
          </GridItemContent>
        </GridItemWrapper>
        <GridItemWrapper key="dark-magician">
          <GridItemContent>Washing Machine
          <center>
            <div><img src="https://www.voltasbeko.com/media/catalog/product/v/w/vwm915647-final-copy.jpg" alt="" height="150px" width="150px"/></div>
            Name: Samsung Washing Machine
            <div>Description: Fully Automatic, Fast Dry Technology</div>
            <div>Manufacture Year:2022</div>
            <div>Base Price:44,499</div>
            <div>Owner: Karan K.</div>
            </center>
          </GridItemContent>
        </GridItemWrapper>
        <GridItemWrapper key="kuriboh">
          <GridItemContent>Air Conditionar
          <center>
            <div><img src="https://www.orissapost.com/wp-content/uploads/2019/05/AIR-CONDITIONERS-1024x860.jpg" alt="" height="150px" width="150px"/></div>
            Name: Voltas AC
            <div>Description: All weather Support,fast cooling,Low power Required</div>
            <div>Manufacture Year:2020</div>
            <div>Base Price:84,499</div>
            <div>Owner: Suhas L.</div>
            </center>
          </GridItemContent>
        </GridItemWrapper>
        <GridItemWrapper key="spell-caster">
          <GridItemContent>Road Cycle
          <center>
            <div><img src="http://sc04.alicdn.com/kf/H01837e3c4579485795b82617b228ea8cs.jpg" alt="" height="150px" width="150px"/></div>
            Name: Hero Cycle
            <div>Description: Disc Breaks, 6 Gear Technology</div>
            <div>Manufacture Year:2021</div>
            <div>Base Price:14,499</div>
            <div>Owner: Manish R.</div>
            </center>
          </GridItemContent>
        </GridItemWrapper>
      </GridLayout>
    </Root>
  );
};
export default layout