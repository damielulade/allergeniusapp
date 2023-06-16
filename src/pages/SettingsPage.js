import React from "react";
import MainHeaderVariant from "../components/main/MainHeaderVariant";
import TwoOptionRadioButton from "../components/utility/ViewRadioButton";
import { useState } from "react";
import { useEffect } from "react";
import axios from "axios";
import SettingsGroupCard from "../components/SettingsGroupCard";

export default function SettingsPage() {
  const [data, setData] = useState([]);
  const [filter, setFilter] = useState("Myself")

  useEffect(() => {
    const fetchData = () => {
      axios
        .get(`/api/groups`)
        .then((response) => setData(response.data))
        .catch((error) => console.log(error));
    };
    fetchData();
  }, []);

  useEffect(() => {
    const fetchFilter = () => {
      axios
        .get("/api/current_filter/setting")
        .then((response) => setFilter(response.data))
        .catch((error) => console.log(error));
    };
    fetchFilter();
  }, []);

  const groups = Object.entries(data)
  groups.unshift(["Myself", {}]);

  const cards = groups.map((group, index) => {
    return (
      <SettingsGroupCard
        key={index}
        id={group[0]}
        members={group[1]}
        startState={group[0] === filter}
      />
    );
  });

  return (
    <div className="section">
      <div className="main">
        <MainHeaderVariant />
        <div className="container-other">
          <h2 id="settings-title">Settings</h2>
          <TwoOptionRadioButton option1={"Map View"} option2={"List View"} />
          <div id="filter-type-section">
            <h2 id="settings-title">Filter out allergens by:</h2>
            <form id="settings-group-filter">{cards}</form>
          </div>
        </div>
      </div>
    </div>
  );
}
