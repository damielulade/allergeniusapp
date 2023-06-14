import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import AccountPage from './pages/AccountPage';
import FilterPage from './pages/FilterPage';
import FriendsPage from './pages/FriendsPage';
import MyAllergenPage from './pages/MyAllergenPage';
import PrivacyPage from './pages/PrivacyPage';
import SearchPage from './pages/SearchPage';
import HomePage from './pages/HomePage';
import SettingsPage from './pages/SettingsPage';
import GroupsPage from './pages/GroupsPage';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<HomePage />} />
        <Route path="/account" element={<AccountPage />} />
        <Route path="/filter" element={<FilterPage />} />
        <Route path="/friends" element={<FriendsPage />} />
        <Route path="/allergens" element={<MyAllergenPage />} />
        <Route path="/privacy" element={<PrivacyPage />} />
        <Route path="/search" element={<SearchPage />} />
        <Route path="/settings" element={<SettingsPage />} />
        <Route path='/groups' element={<GroupsPage />} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </BrowserRouter>
    
  )
}