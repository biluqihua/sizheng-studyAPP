<template>
  <div class="profile-page">
    <el-row :gutter="24">
      <!-- 左侧个人信息 -->
      <el-col :xs="24" :md="8">
        <el-card class="profile-card">
          <div class="profile-header">
            <el-avatar :size="100" class="profile-avatar">
              {{ userStore.userInfo?.name?.charAt(0) || '用' }}
            </el-avatar>
            <h2 class="profile-name">{{ userStore.userInfo?.name }}</h2>
            <p class="profile-id">学号：{{ userStore.userInfo?.student_id }}</p>
          </div>
          <div class="profile-stats">
            <div class="stat-item">
              <div class="stat-value">{{ energyBalance }}</div>
              <div class="stat-label">研习能量</div>
            </div>
            <div class="stat-item">
              <div class="stat-value">0</div>
              <div class="stat-label">学习天数</div>
            </div>
            <div class="stat-item">
              <div class="stat-value">0</div>
              <div class="stat-label">勋章数</div>
            </div>
          </div>
        </el-card>

        <el-card class="profile-section" style="margin-top: 24px">
          <template #header>
            <div class="card-header">
              <el-icon color="#3b82f6"><Trophy /></el-icon>
              <span>快捷操作</span>
            </div>
          </template>
          <div class="profile-actions">
            <el-button type="primary" style="width: 100%" @click="handleCheckIn">
              <el-icon><Calendar /></el-icon>
              每日签到
            </el-button>
            <el-button style="width: 100%; margin-top: 12px" @click="viewEnergyRecords">
              <el-icon><Document /></el-icon>
              积分记录
            </el-button>
          </div>
        </el-card>
      </el-col>

      <!-- 右侧内容 -->
      <el-col :xs="24" :md="16">
        <el-card class="profile-section">
          <template #header>
            <div class="card-header">
              <el-icon color="#3b82f6"><User /></el-icon>
              <span>个人信息</span>
            </div>
          </template>
          <el-descriptions :column="1" border>
            <el-descriptions-item label="姓名">{{ userStore.userInfo?.name }}</el-descriptions-item>
            <el-descriptions-item label="学号">{{ userStore.userInfo?.student_id }}</el-descriptions-item>
            <el-descriptions-item label="邮箱">{{ userStore.userInfo?.email || '未绑定' }}</el-descriptions-item>
            <el-descriptions-item label="手机">{{ userStore.userInfo?.phone || '未绑定' }}</el-descriptions-item>
            <el-descriptions-item label="角色">
              <el-tag type="primary">{{ userStore.userInfo?.role === 'admin' ? '管理员' : userStore.userInfo?.role === 'teacher' ? '教师' : '学生' }}</el-tag>
            </el-descriptions-item>
            <el-descriptions-item label="注册时间">{{ formatDate(userStore.userInfo?.created_at) }}</el-descriptions-item>
          </el-descriptions>
        </el-card>

        <el-card class="profile-section" style="margin-top: 24px">
          <template #header>
            <div class="card-header">
              <el-icon color="#e74c3c"><Document /></el-icon>
              <span>积分记录</span>
            </div>
          </template>
          <el-table :data="energyRecords" stripe>
            <el-table-column prop="change_type" label="类型" width="120">
              <template #default="{ row }">
                <el-tag :type="row.amount > 0 ? 'success' : 'danger'">
                  {{ row.amount > 0 ? '+' : '' }}{{ row.amount }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column prop="description" label="说明" />
            <el-table-column prop="balance" label="余额" width="100" />
            <el-table-column prop="created_at" label="时间" width="180">
              <template #default="{ row }">
                {{ formatDate(row.created_at) }}
              </template>
            </el-table-column>
          </el-table>
        </el-card>

        <el-card class="profile-section" style="margin-top: 24px">
          <template #header>
            <div class="card-header">
              <el-icon color="#6b7280"><Setting /></el-icon>
              <span>账户设置</span>
            </div>
          </template>
          <div class="settings-actions">
            <el-button type="danger" @click="handleLogout">
              <el-icon><SwitchButton /></el-icon>
              退出登录
            </el-button>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import { useUserStore } from '@/stores/user'
import request from '@/utils/request'
import { Trophy, User, Calendar, Document, Setting, SwitchButton } from '@element-plus/icons-vue'

const router = useRouter()
const userStore = useUserStore()
const energyBalance = ref(0)
const energyRecords = ref([])

const loadEnergyData = async () => {
  try {
    const [balanceRes, recordsRes] = await Promise.all([
      userStore.getBalance(),
      request.get('/energy/records', { params: { limit: 10 } })
    ])
    energyBalance.value = balanceRes.balance || userStore.userInfo?.energy_balance || 0
    energyRecords.value = recordsRes
  } catch (error) {
    console.error(error)
  }
}

const handleCheckIn = async () => {
  try {
    const res = await request.post('/energy/check-in')
    ElMessage.success(`签到成功！获得 ${res.energy_awarded} 积分，连续 ${res.streak_days} 天`)
    loadEnergyData()
  } catch (error) {
    if (error.response?.status === 400) {
      ElMessage.warning(error.response?.data?.detail || '今天已签到')
    }
  }
}

const viewEnergyRecords = () => {
  loadEnergyData()
  ElMessage.info('已刷新积分记录')
}

const handleLogout = async () => {
  try {
    await ElMessageBox.confirm('确定要退出登录吗？', '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    })
    userStore.logout()
    router.push('/login')
    ElMessage.success('已退出登录')
  } catch (error) {
    if (error !== 'cancel') {
      console.error(error)
    }
  }
}

const formatDate = (dateStr) => {
  if (!dateStr) return '-'
  return new Date(dateStr).toLocaleString('zh-CN')
}

onMounted(() => {
  energyBalance.value = userStore.userInfo?.energy_balance || 0
  loadEnergyData()
})
</script>

<style scoped>
.profile-page {
  padding-bottom: 40px;
}

.profile-card {
  text-align: center;
}

.profile-header {
  padding: 24px 0;
}

.profile-avatar {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  font-size: 40px;
}

.profile-name {
  font-size: 24px;
  color: #1f2937;
  margin: 16px 0 8px;
}

.profile-id {
  color: #6b7280;
  font-size: 14px;
}

.profile-stats {
  display: flex;
  justify-content: space-around;
  padding: 20px 0;
  border-top: 1px solid #f3f4f6;
}

.stat-item {
  text-align: center;
}

.stat-value {
  font-size: 28px;
  font-weight: bold;
  color: #3b82f6;
}

.stat-label {
  font-size: 13px;
  color: #6b7280;
  margin-top: 4px;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
}

.profile-actions, .settings-actions {
  padding: 12px 0;
}
</style>
