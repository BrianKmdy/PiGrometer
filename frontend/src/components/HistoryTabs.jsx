import React, {useEffect, useState} from 'react';
import { Tabs, TabList, TabPanels, Tab, TabPanel } from '@chakra-ui/react'

const HistoryTabs = ({history}) => {
    return (
        <Tabs variant='soft-rounded' colorScheme='purple'>
        <TabList>
            <Tab>Today</Tab>
            <Tab>Past 3 days</Tab>
            <Tab>Past 7 days</Tab>
        </TabList>
        <TabPanels>
            <TabPanel>
            <p>Today</p>
            </TabPanel>
            <TabPanel>
            <p>Past 3 days</p>
            </TabPanel>
            <TabPanel>
            <p>Past 7 days</p>
            </TabPanel>
        </TabPanels>
        </Tabs>
    )
}

export default HistoryTabs;